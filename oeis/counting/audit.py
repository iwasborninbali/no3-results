#!/usr/bin/env python3
"""Audit provenance and the actual validation-before-production ordering."""
import argparse
import datetime
import hashlib
import json
from pathlib import Path
from collect import atomic_json, aggregate, sha


def audit(base, source):
    base, source = Path(base), Path(source)
    manifest = json.loads((base/'build-manifest.json').read_text())
    checked, unavailable = [], []
    for name, expected in manifest['sha256'].items():
        candidate = base/name
        if not candidate.exists():
            candidate = source/name
        if candidate.is_file():
            assert sha(candidate) == expected, ('build hash mismatch', name)
            checked.append(name)
        else:
            unavailable.append(name)
    build_sha = sha(base/'build-manifest.json')
    validation = json.loads((base/'validation.json').read_text())
    assert validation['build_sha256'] == build_sha
    assert validation['status'] == 'exact (two programs agree)' and validation['n'] == [8, 9]
    events = [json.loads(s) for s in (base/'ledger.jsonl').read_text().splitlines() if s.strip()]
    launch = next(e for e in events if e['event'] == 'n10_launch')
    assert launch['validation_sha256'] == sha(base/'validation.json')
    completed_validation = {e['n']: e['utc'] for e in events if e['event'] == 'grid_validated' and e['n'] in [8, 9]}
    assert len(completed_validation) == 2
    assert all(t <= validation['validated_utc'] <= launch['utc'] for t in completed_validation.values())
    starts10 = [e for e in events if e['event'] == 'start' and e.get('n') == 10]
    assert starts10 and min(e['utc'] for e in starts10) >= launch['utc']
    assert not any(e['event'] == 'start' and e.get('n') == 11 for e in events)
    for n in [8, 9, 10]:
        plan = json.loads((base/f'run-n{n}'/'plan.json').read_text())
        assert plan['build_sha256'] == build_sha
        p = 1+n+n*(n-1)//2
        patterns = [0]+[1<<i for i in range(n)]+[(1<<i)|(1<<j) for i in range(n) for j in range(i+1,n)]
        def reflect(x):
            return sum(((x>>i)&1)<<(n-1-i) for i in range(n))
        c = sum(x <= reflect(x) for x in patterns)
        for program, expected in [('row', c+(c-1)*p), ('det', p*p)]:
            for path in (base/f'run-n{n}'/program).glob('*.receipt.json'):
                d = json.loads(path.with_name(path.name.removesuffix('.receipt.json')+'.json').read_text())
                assert d['frontiers'] == expected, ('analytic frontier count', n, program)
    exact = {str(n): aggregate(base/f'run-n{n}', source/'reference'/f'n{n}.json', True)['status'] for n in [8, 9]}
    current = aggregate(base/'run-n10')
    return {'audited_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'validation': exact, 'n10_status': current['status'],
            'validation_before_n10_launch': True, 'n10_launch_utc': launch['utc'],
            'first_n10_start_utc': min(e['utc'] for e in starts10),
            'no_n11_enumeration_in_queue_ledger': True,
            'analytic_frontier_counts_checked': True,
            'verified_manifest_files': checked, 'unavailable_manifest_files': unavailable,
            'unavailable_note': 'VM binaries are not copied to the Mac; executed binary hashes remain in the build manifest.'}


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--base', default='vm-results')
    p.add_argument('--source', default='.')
    p.add_argument('--output', default='audit.json')
    a = p.parse_args()
    d = audit(a.base, a.source)
    atomic_json(a.output, d)
    print(json.dumps(d, indent=2))
