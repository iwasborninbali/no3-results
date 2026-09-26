#!/usr/bin/env python3
"""Coverage check of the n = 9 re-run of the shipped second solver (cyc3d_mine.c) as 8 receipted shards (first chosen orbit index
modulo 8; incumbent 23, target 24, no time limit reached; seconds are each process's elapsed wall time, CLOCK_MONOTONIC).
usage: python3 coverage_n9_rerun.py <receipt dir> [<summary.json>]     (exit 0 only when all 8 shards are present and exhausted)"""
import sys, os, re, json, hashlib
d = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
rows = {}; problems = []
for s in range(8):
    f = f'{d}/receipt_n9_shard{s}of8.txt'
    if not os.path.exists(f): problems.append(('missing', s)); continue
    t = open(f, encoding='utf-8', errors='replace').read()
    m = re.search(r'n=9 орбит=(\d+) доля=(\d+)/(\d+)\.(-?\d+)/(\d+) нач\.лучшее=(\d+): (ИСЧЕРПАНО|ОБОРВАНО) — (НЕ ПРЕВЗОШЁЛ НАЧАЛЬНОГО|МАКСИМУМ \d+).*?узлов (\d+), ([\d.]+)с', t, re.S)
    if not m: problems.append(('unparsable', s)); continue
    orb, sh, nsh, sh2, nsh2, best0, status, outcome, nodes, secs = m.groups()
    if (int(sh), int(nsh), int(best0)) != (s, 8, 23): problems.append(('wrong partition line', s, m.group(0)[:80]))
    if status != 'ИСЧЕРПАНО' or not outcome.startswith('НЕ ПРЕВЗОШЁЛ'): problems.append(('not exhausted or exceeded', s, status, outcome))
    rows[s] = {'orbits': int(orb), 'nodes': int(nodes), 'seconds': float(secs), 'sha256': hashlib.sha256(open(f, 'rb').read()).hexdigest()}
total_nodes = sum(r['nodes'] for r in rows.values()); total_secs = sum(r['seconds'] for r in rows.values())
summary = {'shards_expected': 8, 'shards_exhausted': len(rows) - sum(1 for p in problems if p[0] == 'not exhausted or exceeded'), 'problems': problems,
           'total_nodes': total_nodes, 'total_wall_seconds_summed': round(total_secs, 1), 'total_process_hours': round(total_secs / 3600, 2),
           'max_shard_seconds': max((r['seconds'] for r in rows.values()), default=None), 'orbits': sorted({r['orbits'] for r in rows.values()}),
           'receipts': {f'{s}/8': rows[s] for s in sorted(rows)}}
print(json.dumps({k: v for k, v in summary.items() if k != 'receipts'}, ensure_ascii=False))
if len(sys.argv) > 2: json.dump(summary, open(sys.argv[2], 'w'), ensure_ascii=False, indent=1)
sys.exit(0 if not problems and len(rows) == 8 else 1)
