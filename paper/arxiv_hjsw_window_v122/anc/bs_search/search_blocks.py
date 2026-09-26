"""Finite BS evidence in the HJSW window; BS remains open.
Run from anc: python3 bs_search/search_blocks.py --verify
Optional regeneration: python3 bs_search/search_blocks.py 503
Floating solvers propose candidates only; integer/Fraction checks certify bounds.
Verification needs only the standard library. Regeneration needs NumPy and SciPy.
"""
import sys, json, hashlib, math
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict, Counter
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parent
TABLE=ROOT.parent/'slack/t221/standard_model.json'

def primes(n):
    return [p for p in range(3,n+1,2) if all(p%d for d in range(3,math.isqrt(p)+1,2))]

def blocks(p):
    roots={i*i%p:i for i in range((p+1)//2)}
    for t in sorted(roots):
        if (t-1)%p in roots: continue
        run=[];u=t
        while u in roots: run.append(u);u=(u+1)%p
        if len(run)<2 or 0 in run:continue
        vs=[roots[t] for t in run];pts=set();bits=''
        X=lambda x: (x+(p-1)//2)%p-(p-1)//2
        for u,v in zip(vs,vs[1:]):
            a,b=(u+v)%p,(v-u)%p
            assert a*b%p==1
            bits+=str(int(X(a)*X(b)<0))
            for c,d in [(a,b),(b,a),(-a%p,-b%p),(-b%p,-a%p)]:
                for i in (0,1):
                    for j in (0,1):
                        x,y=X(c)+i*p,d+j*p
                        pts.add((x,y));pts.add((p-x,y))
        pts=sorted(pts);assert len(pts)==32*(len(run)-1)
        yield run,bits,pts

def lines(pts):
    ls=defaultdict(list)
    for i,(x,y) in enumerate(pts):
        for a,b in [('x',x),('y',y),('d',x-y),('s',x+y)]:ls[a,b].append(i)
    return [v for _,v in sorted(ls.items()) if len(v)>2]

def require(condition, message):
    if not condition:
        raise ValueError(message)


def verify(row):
    p = row['p']
    require(type(p) is int and p in primes(p), 'invalid odd prime')
    require(all(type(t) is int for t in row['run']), 'run entries must be integers')
    found = next((b for b in blocks(p) if b[0] == row['run']), None)
    require(found is not None, 'not a maximal nondegenerate run')
    run, bits, pts = found
    require(bits == row['signature'], 'signature mismatch')
    ls = lines(pts)
    n = len(pts)
    # Check types BEFORE range or incidence tests: bool and fractional values are invalid.
    require(all(type(i) is int for i in row['witness']), 'witness indices must be integers')
    w = set(row['witness'])
    require(len(w) == len(row['witness']), 'duplicate witness index')
    require(all(0 <= i < n for i in w), 'witness index out of range')
    require(all(sum(i in w for i in line) <= 2 for line in ls), 'infeasible witness')
    ys = [F(a) for a in row['dual']]
    require(len(ys) == len(ls) and all(y >= 0 for y in ys), 'invalid dual multipliers')
    cov = [F(0) for _ in pts]
    for y, line in zip(ys, ls):
        for i in line:
            cov[i] += y
    upper = 2*sum(ys) + sum(max(F(0), 1-c) for c in cov)
    require(str(upper) == row['upper'], 'upper bound mismatch')
    interval = [len(w), upper.numerator // upper.denominator]
    require(interval[0] <= interval[1], 'inconsistent bounds')
    require(all(type(i) is int for i in row['beta_interval']), 'interval endpoints must be integers')
    require(interval == row['beta_interval'], 'beta interval mismatch')
    return tuple(interval)


def verify_dataset(data, expected_limit=503):
    require(type(data['prime_limit']) is int and data['prime_limit'] == expected_limit,
            'prime limit mismatch')
    expected = {(p, tuple(run)) for p in primes(expected_limit) for run, _, _ in blocks(p)}
    seen = set()
    by_signature = defaultdict(set)
    exact = table_blocks = table_proved = 0
    lengths, signatures, violations = set(), set(), []
    table = json.loads(TABLE.read_text())
    for index, row in enumerate(data['rows']):
        low, high = verify(row)
        key = row['p'], tuple(row['run'])
        require(key in expected, 'unexpected block')
        require(key not in seen, 'duplicate block')
        seen.add(key)
        bits = row['signature']
        k = len(row['run'])
        half = 16*(k-1)
        lengths.add(k)
        signatures.add(bits)
        if low == high:
            exact += 1
            by_signature[bits].add(half-low)
        if k <= 9:
            table_blocks += 1
            require(bits in table, 'missing reference table signature')
            target = half-F(str(min(table[bits])))
            table_proved += high <= target
            if low > target:
                violations.append(dict(kind='table_lower_bound', row=index))
        if len(by_signature[bits]) > 1:
            violations.append(dict(kind='signature_invariance', signature=bits,
                                   values=sorted(by_signature[bits])))
    require(seen == expected, 'incomplete block list')
    # Access to an unresolved signature above creates an empty set, as in the original search.
    saved = {k: sorted(v) for k, v in sorted(by_signature.items())}
    summary = dict(prime_limit=expected_limit, blocks=len(seen), exact_optima=exact,
                   unresolved_gaps=len(seen)-exact, violations=violations,
                   certified_savings=saved)
    for key, value in summary.items():
        require(data[key] == value, 'summary mismatch: '+key)
    summary.update(odd_primes=len(primes(expected_limit)), min_length=min(lengths),
                   max_length=max(lengths), signatures=len(signatures),
                   table_blocks=table_blocks, table_certified=table_proved,
                   table_unresolved=table_blocks-table_proved)
    return {k: v for k, v in summary.items() if k != 'certified_savings'}


def main(limit):
    import numpy as np
    from scipy.optimize import milp, linprog, LinearConstraint, Bounds
    table=json.loads(TABLE.read_text())
    rows=[];exact=0;violations=[];cert_by_sig=defaultdict(set);uncertain=0
    for p in primes(limit):
        for run,bits,pts in blocks(p):
            ls=lines(pts);n=len(pts);a=np.zeros((len(ls),n))
            for i,l in enumerate(ls):a[i,l]=1
            lp=linprog(-np.ones(n),A_ub=a,b_ub=np.full(len(ls),2),bounds=(0,1),method='highs')
            assert lp.success
            ys=[max(F(0),F(float(-v)).limit_denominator(10000)) for v in lp.ineqlin.marginals]
            cov=[sum((ys[i] for i,l in enumerate(ls) if j in l),F(0)) for j in range(n)]
            upper=2*sum(ys)+sum(max(F(0),1-c) for c in cov)
            ip=milp(-np.ones(n),integrality=np.ones(n),bounds=Bounds(0,1),constraints=LinearConstraint(a,-np.inf,2),options={'node_limit':2000,'mip_rel_gap':0.0})
            if ip.x is None:raise RuntimeError((p,run,ip.message))
            witness=np.flatnonzero(ip.x>.5).tolist()
            row=dict(p=p,run=run,signature=bits,witness=witness,dual=list(map(str,ys)),upper=str(upper))
            row['beta_interval']=[len(witness), upper.numerator//upper.denominator]
            low,hi=verify(row)
            if low==hi: exact+=1;cert_by_sig[bits].add(n//2-low)
            else:uncertain+=1
            if bits in table and low>n//2-min(table[bits]):violations.append(dict(kind='table_lower_bound',row=len(rows)))
            if len(cert_by_sig[bits])>1:violations.append(dict(kind='signature_invariance',signature=bits,values=sorted(cert_by_sig[bits])))
            rows.append(row)
        if p%50<6:print('p',p,'blocks',len(rows),'exact',exact,'gaps',uncertain,'violations',violations,flush=True)
    result=dict(prime_limit=limit,blocks=len(rows),exact_optima=exact,unresolved_gaps=uncertain,violations=violations,certified_savings={k:sorted(v) for k,v in sorted(cert_by_sig.items())},rows=rows)
    verify_dataset(result, expected_limit=limit)
    out=ROOT/'block_search.json';out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('rows','certified_savings')},indent=2))
    print('SHA256',hashlib.sha256(out.read_bytes()).hexdigest(),str(out.relative_to(ROOT)))

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--verify':
        source = Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT/'block_search.json'
        result = verify_dataset(json.loads(source.read_text()))
        print(json.dumps(result, sort_keys=True))
        print('EXACT VERIFICATION PASSED', result['blocks'])
    else:
        main(int(sys.argv[1]) if len(sys.argv) > 1 else 503)
