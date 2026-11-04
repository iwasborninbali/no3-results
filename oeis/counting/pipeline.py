#!/usr/bin/env python3
"""Four-worker durable queue; validation gates production. Safe to restart."""
import concurrent.futures
import datetime
import fcntl
import hashlib
import json
import os
from pathlib import Path
import random
import subprocess
import time
from collect import aggregate, atomic_json, read_shard, sha

BASE = Path(__file__).resolve().parent
os.chdir(BASE)
BUILD = sha('build-manifest.json')


def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def event(value):
    value = {'utc': utc(), **value}
    with open('ledger.jsonl', 'a') as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        f.write(json.dumps(value) + '\n')
        f.flush()
        os.fsync(f.fileno())
    print(json.dumps(value), flush=True)


def run_shard(root, plan, program, shard):
    if read_shard(root, plan, program, shard) is not None:
        return
    stem = root / program / f'{shard:04d}'
    stem.parent.mkdir(parents=True, exist_ok=True)
    n, shards, split = plan['n'], plan['shards'], plan['split_rows']
    command = ['./line_rows', str(n), '--shard', str(shard), '--shards', str(shards), '--split-rows', str(split)] if program == 'row' else [
        './determinant_check', str(n), str(shard), str(shards), str(split)]
    rec = {'state': 'running', 'program': program, 'n': n, 'shard': shard,
           'command': command, 'build_sha256': BUILD, 'started_utc': utc()}
    event({'event': 'start', 'n': n, 'program': program, 'shard': shard})
    began = time.monotonic()
    with open(stem.with_suffix('.json.part'), 'w') as out, open(stem.with_suffix('.log'), 'w') as err:
        proc = subprocess.Popen(command, stdout=out, stderr=err, start_new_session=True)
        rec['pid'] = proc.pid
        atomic_json(stem.with_suffix('.running.json'), rec)
        rc = proc.wait()
        out.flush()
        os.fsync(out.fileno())
    rec.update(exit_code=rc, ended_utc=utc(), wall_seconds=time.monotonic()-began)
    if rc:
        rec['state'] = 'failed'
        atomic_json(stem.with_suffix('.failed.json'), rec)
        event({'event': 'failed', 'n': n, 'program': program, 'shard': shard, 'exit_code': rc})
        raise RuntimeError(f'{command}: exit {rc}')
    # Parsing and metadata checks happen before a successful receipt is issued.
    d = json.loads(stem.with_suffix('.json.part').read_text())
    assert d['n'] == n and d['shard'] == shard and d['shards'] == shards and d['program'] == program
    stem.with_suffix('.json.part').replace(stem.with_suffix('.json'))
    rec.update(state='complete', output_sha256=sha(stem.with_suffix('.json')))
    atomic_json(stem.with_suffix('.receipt.json'), rec)
    read_shard(root, plan, program, shard)
    stem.with_suffix('.running.json').unlink(missing_ok=True)
    event({'event': 'complete', 'n': n, 'program': program, 'shard': shard,
           'cpu_seconds': d['cpu_seconds'], 'wall_seconds': rec['wall_seconds'],
           'work': d.get('prefix_leaves', d.get('visits'))})


def run_grid(n, shards):
    root = BASE / f'run-n{n}'
    root.mkdir(exist_ok=True)
    plan = {'n': n, 'shards': shards, 'split_rows': 2, 'workers': 4,
            'build_sha256': BUILD, 'shuffle_seed': 2026110400+n}
    pp = root / 'plan.json'
    if pp.exists():
        assert json.loads(pp.read_text()) == plan
    else:
        atomic_json(pp, plan)
    # Randomized order supplies reasonably representative completed-shard timing
    # samples. Both programs share four slots; no oversubscription by this queue.
    ids = list(range(shards))
    random.Random(plan['shuffle_seed']).shuffle(ids)
    jobs = [(program, shard) for shard in ids for program in ['row', 'det']]
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        futures = [pool.submit(run_shard, root, plan, program, shard) for program, shard in jobs]
        for f in concurrent.futures.as_completed(futures):
            f.result()
    ref = BASE / 'reference' / f'n{n}.json' if n in (8, 9) else None
    result = aggregate(root, ref, require_complete=True)
    event({'event': 'grid_validated', 'n': n, 'status': result['status']})


def estimates():
    Path('estimates').mkdir(exist_ok=True)
    jobs = [(n, seed) for n in (8, 9, 10, 11) for seed in (202611041, 202611042, 202611043)]
    def one(job):
        n, seed = job
        out = Path(f'estimates/n{n}-{seed}.json')
        if out.exists():
            json.loads(out.read_text())
            return
        with open(out.with_suffix('.part'), 'w') as f:
            subprocess.run(['./tree_estimate', str(n), '1000000', str(seed)], stdout=f, check=True)
        out.with_suffix('.part').replace(out)
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        list(pool.map(one, jobs))
    event({'event': 'estimates_complete'})


if __name__ == '__main__':
    lock = open('pipeline.lock', 'w')
    fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    atomic_json('pipeline.pid.json', {'pid': os.getpid(), 'started_utc': utc(), 'build_sha256': BUILD})
    event({'event': 'pipeline_start', 'pid': os.getpid(), 'workers': 4})
    run_grid(8, 32)
    run_grid(9, 64)
    atomic_json('validation.json', {'status': 'exact (two programs agree)', 'validated_utc': utc(),
                                   'n': [8, 9], 'build_sha256': BUILD,
                                   'checks': 'all T/M cells match prior exact profiles; exact row-node and leaf ledgers; direct addable-point ledger in both programs'})
    estimates()
    event({'event': 'n10_launch', 'validation_sha256': sha('validation.json')})
    run_grid(10, 512)
    event({'event': 'pipeline_complete'})
