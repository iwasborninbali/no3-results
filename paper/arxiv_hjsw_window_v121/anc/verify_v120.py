"""New v1.20 exact checks of the repaired formulas; standard library only."""
from itertools import combinations
from math import gcd, factorial
from fractions import Fraction as F
from collections import defaultdict
from pathlib import Path
import json
# Integer incidences, without importing the author's line builder.
p=5; pts=[(x,y) for x in range(-2,8) for y in range(10) if y%p==pow(x,3,p)]
lines=defaultdict(set)
for i,j in combinations(range(len(pts)),2):
 x,y=pts[i]; X,Y=pts[j]; a,b=Y-y,x-X;c=a*x+b*y;d=gcd(gcd(abs(a),abs(b)),abs(c));a,b,c=a//d,b//d,c//d
 if a<0 or (a==0 and b<0):a,b,c=-a,-b,-c
 lines[a,b,c].update((i,j))
masks=[sum(1<<i for i in inds) for inds in lines.values() if len(inds)>=3]
def lawful(inds):
 m=sum(1<<i for i in inds)
 return all((m&line).bit_count()<=2 for line in masks)
witness=next(c for c in combinations(range(20),12) if lawful(c))
assert not any(lawful(c) for c in combinations(range(20),13))
print('Exact p=5 cubic maximum: 12; no lawful 13-subset. Witness:',[pts[i] for i in witness])
for p in (101,1009,1013):
 n=sum(1+(0 if (d:=(4-3*u*u)%p)==0 else (1 if pow(d,(p-1)//2,p)==1 else -1)) for u in range(p))
 chi=1 if pow(p-3,(p-1)//2,p)==1 else -1
 assert n==p-chi
 print('FE conic',p,'points',n,'= p - chi(-3)')
for p in (101,107):
 for a in (1,2):
  for i,j in ((1,3),(2,3)):
   for u in range(1,p):
    x=-(i+j)*u*pow(3,-1,p)%p
    v=(a*pow(x+i*u,3,p)-a*pow(x,3,p))*pow(i,-1,p)%p
    assert v==a*(i*i-i*j+j*j)*pow(u,3,p)*pow(3,-1,p)%p
print('Corrected direction formula: all u, p=101,107; a=1,2; families (1,3),(2,3).')
A=(-4,-1,5)
for m,mp in combinations(range(3),2):
 r=F(A[m],A[mp]);C=set(map(F,A))|{r*c for c in A}
 assert len(C)==5 and len({c*c for c in C})==5
 print('Pair configuration',m+1,mp+1,'ratio',r,'coefficients',sorted(map(str,C)))
tail=F(10,2**9) # sum_{k>=10}(k-1)/2^k = 10/2^9, by geometric differentiation
assert tail==F(5,256)
discrepancy=F('0.028')-F('0.0212');margin=F('0.098')-F(1,12)
print('Exact tail',tail,'=',float(tail),'margin/discrepancy',margin/discrepancy,'=',float(margin/discrepancy))
print('Coefficients:',F(11,4)-F('0.098'),F(11,4)-F('0.093'))
c11=F(126762273520591,45193226158080)
assert c11+2*F(2**14*16,factorial(12))+F(2,factorial(10))+F(8,factorial(11))<F('2.81')
print('C11 plus twice the convergence error and the full-split correction < 2.81: exact rational check passed.')
print('ALL v1.20 checks passed')
