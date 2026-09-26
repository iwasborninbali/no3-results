"""Run every jobs.json entry with the documented interpreter. Offline, anc-local writes only.
Usage: python3 run_all.py [JOB ...]
"""
from pathlib import Path
import concurrent.futures, importlib.util, json, os, subprocess, sys, time
ROOT=Path(__file__).resolve().parent
if Path.cwd()!=ROOT:raise SystemExit('Run from anc/')
PY=sys.executable
jobs=json.loads((ROOT/'jobs.json').read_text())
(RootRuns:=ROOT/'runs').mkdir(exist_ok=True)
selected=sys.argv[1:] or list(jobs)
env=os.environ.copy();env['PYTHONDONTWRITEBYTECODE']='1';env['OPENBLAS_NUM_THREADS']='1';env['OMP_NUM_THREADS']='1'
def run(id):
 j=jobs[id];cmd=[PY,'run_one.py',id]
 if j['skip'] and importlib.util.find_spec('pysat') is None:
  return {'job':id,'command':['python3', 'run_one.py', id],'exit_code':None,'seconds':0,'status':'NOT RUN','reason':j['skip'],'log':None}
 t=time.monotonic()
 path=RootRuns/(id+'.log')
 with path.open('w') as f:
  try:r=subprocess.run(cmd,stdout=f,stderr=subprocess.STDOUT,cwd=ROOT,env=env,timeout=2400);rc=r.returncode
  except subprocess.TimeoutExpired:rc=124
 return {'job':id,'command':['python3', 'run_one.py', id],'exit_code':rc,'seconds':round(time.monotonic()-t,3),'status':'PASS' if rc==0 else 'FAILED','log':str(path.relative_to(ROOT))}
results=[]
old_results=json.loads((RootRuns/'results.json').read_text()) if sys.argv[1:] and (RootRuns/'results.json').exists() else []
old_results=[r for r in old_results if r['job'] not in selected]
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
 for r in ex.map(run,selected):
  results.append(r);print(r['job'],r['status'],r['seconds'],flush=True)
  (RootRuns/'results.json').write_text(json.dumps(old_results+results,indent=2)+'\n')
print('FINISHED',len(results),'jobs',flush=True)
