"""Independent exact arithmetic for the printed finite constants; no solver calls."""
from fractions import Fraction as F
from math import factorial,comb
from collections import Counter
from itertools import permutations
import json,hashlib
from pathlib import Path
OUT=Path(__file__).parent

def add(p,q):
 r=p.copy()
 for m,c in q.items(): r[m]=r.get(m,F(0))+c
 return {m:c for m,c in r.items() if c}
def scale(p,c): return {m:v*c for m,v in p.items() if v*c}
def mul(p,q):
 r={}
 for (i,j),a in p.items():
  for (k,l),b in q.items(): r[(i+k,j+l)]=r.get((i+k,j+l),F(0))+a*b
 return r
def power(p,n):
 r={(0,0):F(1)}
 for _ in range(n):r=mul(r,p)
 return r
def affine(a,b,c):return {(0,0):F(a),(1,0):F(b),(0,1):F(c)}
def integrate_region(p,low,high,ulo,uhi):
 total=F(0)
 for (i,j),v in p.items():
  # g integral has affine-u endpoints; then integrate u exactly.
  for (h,k),c in add(power(high,j+1),scale(power(low,j+1),-1)).items():
   assert k==0
   n=i+h+1
   total+=v*c/F(j+1)* (F(uhi)**n-F(ulo)**n)/n
 return total

def constant(k):
 P=[sum((F((-1)**i,factorial(i)*factorial(j)) for i in range(k-j+1)),F(0)) for j in range(k+1)]
 def ab(q):
  A={};B={}
  for j in range(1,k+1):
   for n in range(1,j+1):
    prob=scale(mul(power(q,n-1),power(add(affine(1,0,0),scale(q,-1)),j-n)),j*P[j]*comb(j-1,n-1))
    if j+n<=3:A=add(A,prob)
    B=add(B,scale(prob,int(n<=3)+int(2*j-n<=3)))
  return A,B
 # Four regions, each split where needed into trapezoids, in (u,g).
 z=affine(0,0,0); one=affine(1,0,0)
 regions=[(affine(1,0,-1),affine(0,2,1),[(z,affine(1,-2,0),0,F(1,2))]),
 (affine(1,0,-1),affine(2,-2,-1),[(affine(1,-2,0),affine(1,-1,0),0,F(1,2)),(z,affine(1,-1,0),F(1,2),1)]),
 (affine(0,0,1),affine(-1,2,1),[(affine(1,-1,0),one,0,F(1,2)),(affine(1,-1,0),affine(2,-2,0),F(1,2),1)]),
 (affine(0,0,1),affine(3,-2,-1),[(affine(2,-2,0),one,F(1,2),1)])]
 U=F(0)
 for qp,qm,traps in regions:
  ap,bp=ab(qp);am,bm=ab(qm)
  integrand=add(mul(ap,bm),mul(am,bp))
  U+=sum((integrate_region(integrand,*t) for t in traps),F(0))
 L=2*sum((P[j]*F(sum(int(n>=4)+int(j+n>=4)+int(2*j-n>=4)+int(j-n>=4) for n in range(j+1)),j+1) for j in range(1,k+1)),F(0))
 return {'k':k,'L':str(L),'U':str(U),'C':str(2*L+U),'C_decimal':float(2*L+U)}

p=OUT.parent/'slack/t221/standard_model.json'
d=json.loads(p.read_text());total=F(0);by_k=[]
for k in range(2,10):
 counts=Counter(''.join('1' if a>b else '0' for a,b in zip(q,q[1:])) for q in permutations(range(k)))
 assert len(counts)==2**(k-1)
 term=F(0)
 for key,n in counts.items():
  term+=F(n,factorial(k)*2**(k+2))*F(str(min(d[key])))
 total+=term;by_k.append({'k':k,'term':str(term)})
assert total==F(68350729,123863040)
cs=[constant(k) for k in (3,5,7,9,11)]
for row,expected in zip(cs,['11/4','28183/10080','15265237/5443200','94048104091/33530112000']):assert row['C']==expected,(row,expected)
r={'block':{'source':p.relative_to(OUT.parent).as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'ambiguous_signatures':{k:v for k,v in d.items() if len(v)>1},'selection':'minimum observed value, matching the cited constant2.py; not a certified universal lower bound','by_k':by_k,'saving':str(total),'upper':str(4-total),'tail_if_claimed_bound_holds':str(F(10,512)),'lower_if_claimed_bound_holds':str(4-total-F(10,512))},'monomial_constants':cs,'limits':'Arithmetic conditional on the supplied block savings and stated local-law integrands; does not prove either model.'}
(OUT/'constants.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
