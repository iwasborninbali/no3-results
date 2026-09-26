"""Independent finite checks for V-L37; no imports from the author's programs."""
from pathlib import Path
from itertools import combinations
from collections import defaultdict, Counter
from functools import lru_cache
from math import gcd, prod
import hashlib, json, subprocess, zipfile

OUT=Path(__file__).resolve().parent
def lines(points):
    d=defaultdict(set)
    for i,j in combinations(range(len(points)),2):
        x,y=points[i]; X,Y=points[j]
        a,b=Y-y,x-X; c=a*x+b*y
        g=gcd(gcd(abs(a),abs(b)),abs(c)); a,b,c=a//g,b//g,c//g
        if a<0 or (a==0 and b<0): a,b,c=-a,-b,-c
        d[a,b,c].update((i,j))
    return [(key,frozenset(v)) for key,v in d.items() if len(v)>=3]

@lru_cache(None)
def exact(n,masks,capacity):
    best=-1; count=0; witness=0
    for s in range(1<<n):
        size=s.bit_count()
        if size<best: continue
        if any((s&m).bit_count()>capacity for m in masks):continue
        if size>best:best,count,witness=size,0,s
        count+=1
    return best,count,witness

def measure(p,c,x0,y0,hjsw=False):
    pts=[(x,y) for x in range(x0,x0+2*p) for y in range(y0,y0+2*p) if x*y%p==c]
    ls=lines(pts)
    assert len(pts)==4*(p-1)
    assert all(a*a==b*b and len(v) in (3,4) for (a,b,C),v in ls)
    groups=defaultdict(list)
    for i,(x,y) in enumerate(pts):
        a,b=x%p,y%p
        key=min((a,b),(b,a),(-a%p,-b%p),(-b%p,-a%p))
        groups[key].append(i)
    s=sum(pow(v,(p-1)//2,p)==1 for v in (c,(-c)%p))
    optimum=0; ways=1; n0=n1=n2=0; exceptional=0
    witness=[]
    for inds in groups.values():
        local={i:j for j,i in enumerate(inds)}
        masks=tuple(sorted(sum(1<<local[i] for i in v) for key,v in ls if v<=local.keys()))
        assert sum(len(v) for key,v in ls if v & local.keys())==sum(m.bit_count() for m in masks)
        val,cnt,w=exact(len(inds),masks,2)
        optimum+=val;ways*=cnt
        witness.extend(pts[inds[j]] for j in range(len(inds)) if w>>j&1)
        if len(inds)==8:
            exceptional+=1;assert val==6 and cnt in (6,9)
        else:
            assert len(inds)==16
            e=sum(len(v)==3 and key[0]==-key[1] for key,v in ls if v<=local.keys())//2
            f=sum(len(v)==3 and key[0]==key[1] for key,v in ls if v<=local.keys())//2
            assert (val,cnt)=={(2,0):(12,1),(0,2):(12,1),(1,1):(10,144),(0,0):(8,1296)}[e,f],(p,c,x0,y0,val,cnt,e,f)
            if (e,f) in ((2,0),(0,2)):n2+=1
            elif (e,f)==(1,1):n1+=1
            else:n0+=1
    assert exceptional==s
    assert optimum==12*n2+10*n1+8*n0+6*s
    assert optimum<=3*(p-1)
    assert not lines(witness)
    quads=[v for key,v in ls if len(v)==4]
    assert sum(map(len,quads))==len(set().union(*quads)) if quads else True
    no4=4*(p-1)-len(quads)
    if hjsw:
        cover=Counter(i for key,v in ls for i in v)
        isolated=len(pts)-len(cover)
        assert optimum==3*(p-1) and ways==9**s
        assert isolated+2*len(ls)==optimum
        assert len(quads)==(p-1)//2-s
        assert no4==(7*(p-1))//2+s
    return {'p':p,'c':c,'x0':x0,'y0':y0,'alpha':optimum,'maxima':ways,'n0':n0,'n1':n1,'n2':n2,'s':s,'alpha_no4':no4,'maxima_no4':4**len(quads)}

rows=[]
for p in (3,5,7,11,13):
    for c in range(1,p):rows.append(measure(p,c,-(p-1)//2,0,True))
for p in (3,5,7):
    for c in range(1,p):
        for x0 in range(p):
            for y0 in range(p):rows.append(measure(p,c,x0,y0))
# Entire shifted-window table in the manuscript.
table=[]
for x in range(11):
    table.append([measure(11,1,x-5,y)['alpha'] for y in range(11)])
expected=[[30,30,30,28,26,24,22,24,26,28,30],[28,28,28,30,28,26,24,26,28,30,28],[26,26,26,28,30,28,26,28,30,28,26],[24,24,24,26,28,30,28,30,28,26,24],[22,22,22,24,26,28,30,28,26,24,22],[22,22,22,24,26,28,30,28,26,24,22],[22,22,22,24,26,28,30,28,26,24,22],[22,22,22,24,26,28,30,28,26,24,22],[24,24,24,26,28,30,28,30,28,26,24],[26,26,26,28,30,28,26,28,30,28,26],[28,28,28,30,28,26,24,26,28,30,28]]
assert table==expected
fe=[]
for p in (101,1009):
    point_count=sum(1+(0 if (d:=(4-3*u*u)%p)==0 else (1 if pow(d,(p-1)//2,p)==1 else -1)) for u in range(p))
    fe.append({'p':p,'points_y2_equals_4_minus_3u2':point_count,'claimed_main':2*p,'correct_main':p})
result={'cases':len(rows),'table_cases':121,'unique_gadgets':exact.cache_info().currsize,'all_passed':True,'fe_countercheck':fe,'rows':rows,'shift_table':table}
(OUT/'results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ('rows','shift_table')},indent=2))
