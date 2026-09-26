"""Execute one documented job from anc, keeping historical evidence read-only.
Usage: python3 run_one.py JOB
"""
from pathlib import Path
import builtins, importlib.util, io, json, os, runpy, sys
ROOT=Path(__file__).resolve().parent
if Path.cwd()!=ROOT: raise SystemExit('Run from anc/')
id=sys.argv[1]
job=json.loads((ROOT/'jobs.json').read_text())[id]
if job['skip'] and importlib.util.find_spec('pysat') is None: raise SystemExit('NOT RUN: '+job['skip'])
# Avoid creating bytecode in the source/data snapshot.
sys.dont_write_bytecode=True
os.environ['PYTHONDONTWRITEBYTECODE']='1'
for d in ['','slack','slack/t221','slack/t221_agents','slack/g39_agents','independent']:
 sys.path.insert(0,str(ROOT/d))
original_open=builtins.open
original_io_open=io.open
output_root=ROOT/'runs/generated'/id
output_root.mkdir(parents=True,exist_ok=True)
def redirected(file,mode='r',*args,**kwargs):
 if isinstance(file,(str,bytes,os.PathLike)) and any(c in mode for c in 'wax+'):
  path=Path(file).resolve()
  try: rel=path.relative_to(ROOT)
  except ValueError: raise RuntimeError('Attempted write outside anc: '+str(path))
  dest=output_root/rel
  dest.parent.mkdir(parents=True,exist_ok=True)
  return original_open(dest,mode,*args,**kwargs)
 return original_open(file,mode,*args,**kwargs)
builtins.open=redirected
io.open=redirected
sys.argv=[job['script']]+job['args']
print('JOB',id,':',job['description'],flush=True)
print('SOURCE',job['script'],'ARGS',job['args'],flush=True)
if job['code']:
 ns=runpy.run_path(str(ROOT/job['script']),run_name='anc_library')
 exec(job['code'],{'ns':ns})
else:
 runpy.run_path(str(ROOT/job['script']),run_name='__main__')
print('JOB COMPLETE',id,flush=True)
