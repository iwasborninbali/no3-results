#!/usr/bin/env python3
"""Verify shard receipts and sum exhaustive results. No approximate counts enter exact output."""
import argparse
import hashlib
import json
import math
from pathlib import Path


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def atomic_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(json.dumps(value, indent=2) + '\n')
    tmp.replace(path)


def read_shard(root, plan, program, shard):
    stem = root / program / f'{shard:04d}'
    receipt_path = stem.with_suffix('.receipt.json')
    if not receipt_path.exists():
        return None
    receipt = json.loads(receipt_path.read_text())
    assert receipt['exit_code'] == 0 and receipt['state'] == 'complete', receipt_path
    assert receipt['build_sha256'] == plan['build_sha256'], receipt_path
    result_path = stem.with_suffix('.json')
    assert sha(result_path) == receipt['output_sha256'], result_path
    d = json.loads(result_path.read_text())
    for key, expected in [('n', plan['n']), ('program', program), ('shard', shard),
                          ('shards', plan['shards']), ('split_rows', plan['split_rows'])]:
        assert d[key] == expected, (result_path, key, d[key], expected)
    size = 2 * plan['n'] + 1
    for key in ['profile', 'maximal_profile', 'freedom_profile']:
        assert len(d[key]) == size
        assert all(type(x) is int and x >= 0 for x in d[key])
    assert sum(d['profile']) == d['total']
    assert sum(d['maximal_profile']) == d['maximal']
    assert all(m <= t for m, t in zip(d['maximal_profile'], d['profile']))
    if program == 'det':
        assert d['visits'] == d['total']
    else:
        assert d['row_nodes'][-1] == d['prefix_leaves']
        assert d['symmetry'] == 1 and d['tail'] == plan['n'] - 1 and d['reverse'] == 0
    return d


def aggregate(root, reference=None, require_complete=False):
    root = Path(root)
    plan = json.loads((root / 'plan.json').read_text())
    n, shards = plan['n'], plan['shards']
    result = {'n': n, 'status': 'estimate', 'shards_per_program': shards,
              'programs': {}, 'checks': []}
    full = []
    for program in ['row', 'det']:
        parts = [d for i in range(shards) if (d := read_shard(root, plan, program, i)) is not None]
        a = {'completed_shards': len(parts), 'complete': len(parts) == shards,
             'cpu_seconds': sum(d['cpu_seconds'] for d in parts),
             'shard_wall_seconds': sum(d['seconds'] for d in parts)}
        for key in ['profile', 'maximal_profile', 'freedom_profile']:
            a[key] = [sum(d[key][k] for d in parts) for k in range(2*n+1)]
        a['total'] = sum(a['profile'])
        a['maximal'] = sum(a['maximal_profile'])
        a['work'] = sum(d['prefix_leaves' if program == 'row' else 'visits'] for d in parts)
        if parts:
            assert len({d['frontiers'] for d in parts}) == 1
            a['frontiers'] = parts[0]['frontiers']
        if a['complete']:
            assert sum(d['assigned_frontiers'] for d in parts) == a['frontiers']
            assert a['profile'][:3] == [1, n*n, math.comb(n*n, 2)]
            triples = sum(1 for p in range(n*n) for q in range(p+1, n*n)
                          for r in range(q+1, n*n)
                          if (q%n-p%n)*(r//n-p//n) == (q//n-p//n)*(r%n-p%n))
            assert a['profile'][3] == math.comb(n*n, 3) - triples
            assert all(a['freedom_profile'][k] == (k+1)*a['profile'][k+1]
                       for k in range(2*n))
            assert a['freedom_profile'][-1] == 0
            endpoint = {8: 380, 9: 368, 10: 1135}.get(n)
            if endpoint is not None:
                assert a['profile'][-1] == a['maximal_profile'][-1] == endpoint
            if reference:
                ref = json.loads(Path(reference).read_text())
                for key in ['profile', 'maximal_profile', 'total', 'maximal']:
                    assert a[key] == ref[key], (program, n, key)
                if program == 'row':
                    assert a['work'] == ref['prefix_leaves']
                    nodes = [sum(d['row_nodes'][r] for d in parts) for r in range(n)]
                    assert nodes == ref['row_nodes'], (n, nodes, ref['row_nodes'])
            a['status'] = 'exact (one program)'
            a['checks'] = ['profile sums', 'maximal bounds', 'frontier partition',
                           'small-k formulas', 'addable-point ledger', 'endpoint']
            full.append(program)
        result['programs'][program] = a
    if full:
        result['status'] = 'exact (one program)'
    if len(full) == 2:
        for key in ['profile', 'maximal_profile', 'freedom_profile', 'total', 'maximal']:
            assert result['programs']['row'][key] == result['programs']['det'][key], key
        result['status'] = 'exact (two programs agree)'
        result['checks'].append('every profile and ledger cell agrees between independent programs')
    if require_complete:
        assert len(full) == 2, 'both programs have not completed'
    atomic_json(root / 'aggregate.json', result)
    return result


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('directory', nargs='?', default='run-n10')
    p.add_argument('--reference')
    p.add_argument('--require-complete', action='store_true')
    args = p.parse_args()
    d = aggregate(args.directory, args.reference, args.require_complete)
    print(json.dumps({'n': d['n'], 'status': d['status'],
                      'programs': {k: {x: v[x] for x in ['completed_shards', 'complete', 'total', 'maximal', 'cpu_seconds', 'work']}
                                   for k, v in d['programs'].items()}}, indent=2))
