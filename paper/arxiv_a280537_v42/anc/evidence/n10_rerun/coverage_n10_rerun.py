#!/usr/bin/env python3
"""Coverage check of the n = 10 re-run of the shipped second solver (cyc3d_mine.c) as 64 receipted shards.
Partition: first chosen orbit index s (mod 8) x second chosen orbit index k (mod 8), one process per (s, k), each
started with the incumbent 26 and target 27, no time limit reached. A shard counts only when its report line says
"ИСЧЕРПАНО" (exhausted) and "НЕ ПРЕВЗОШЁЛ НАЧАЛЬНОГО" (did not exceed the initial incumbent).
usage: python3 coverage_n10_rerun.py <receipt dir>      (exit 0 only when all 64 shards are present and exhausted)"""
import sys, os, re, json, hashlib
d = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
rows = {}; problems = []
for s in range(8):
    for k in range(8):
        f = f'{d}/receipt_n10_shard{s}of8_sub{k}of8.txt'
        if not os.path.exists(f): problems.append(('missing', s, k)); continue
        t = open(f, encoding='utf-8', errors='replace').read()
        m = re.search(r'n=10 орбит=(\d+) доля=(\d+)/(\d+)\.(\d+)/(\d+) нач\.лучшее=(\d+): (ИСЧЕРПАНО|ОБОРВАНО) — (НЕ ПРЕВЗОШЁЛ НАЧАЛЬНОГО|МАКСИМУМ \d+).*?узлов (\d+), ([\d.]+)с', t, re.S)
        if not m: problems.append(('unparsable', s, k)); continue
        orb, sh, nsh, sh2, nsh2, best0, status, outcome, nodes, secs = m.groups()
        if (int(sh), int(nsh), int(sh2), int(nsh2), int(best0)) != (s, 8, k, 8, 26): problems.append(('wrong partition line', s, k, m.group(0)[:80]))
        if status != 'ИСЧЕРПАНО' or not outcome.startswith('НЕ ПРЕВЗОШЁЛ'): problems.append(('not exhausted or exceeded', s, k, status, outcome))
        rows[(s, k)] = {'orbits': int(orb), 'nodes': int(nodes), 'seconds': float(secs), 'sha256': hashlib.sha256(open(f, 'rb').read()).hexdigest()}
total_nodes = sum(r['nodes'] for r in rows.values()); total_secs = sum(r['seconds'] for r in rows.values())
summary = {'shards_expected': 64, 'shards_exhausted': len(rows) - sum(1 for p in problems if p[0] == 'not exhausted or exceeded'), 'problems': problems,
           'total_nodes': total_nodes, 'total_cpu_seconds': round(total_secs, 1), 'total_cpu_hours': round(total_secs / 3600, 2),
           'max_shard_seconds': max((r['seconds'] for r in rows.values()), default=None), 'orbits': sorted({r['orbits'] for r in rows.values()}),
           'receipts': {f'{s}/8.{k}/8': rows[(s, k)] for (s, k) in sorted(rows)}}
print(json.dumps({k: v for k, v in summary.items() if k != 'receipts'}, ensure_ascii=False))
if len(sys.argv) > 2: json.dump(summary, open(sys.argv[2], 'w'), ensure_ascii=False, indent=1)
sys.exit(0 if not problems and len(rows) == 64 else 1)
