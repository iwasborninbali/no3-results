"""Independent exact checks for v1.22; standard library, no solver or network.

Run from anc: python3 verify_v122.py
All arithmetic and the reference block checker below have their own code.
The repaired verifier is loaded only as the subject of regression tests.
These finite checks accompany the proofs; they do not prove BS or original UM.
"""
from collections import Counter, defaultdict
from copy import deepcopy
from fractions import Fraction as F
from importlib.util import module_from_spec, spec_from_file_location
from itertools import permutations
from math import factorial
from pathlib import Path
import json
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent


def floor_integral(q):
    # Integrate on the positive half using exact breakpoints and midpoints.
    breaks = sorted({F(2*q-j, 3*q) for j in range(2*q+1)})
    return 2*sum((b-a)*((q*(2-3*(a+b)/2))//1)/q
                 for a, b in zip(breaks, breaks[1:]))


def weak_margin():
    for q in range(1, 201):
        assert floor_integral(q) == F(4*q-2, 3*q)
    cx, cy = floor_integral(3), floor_integral(63)
    assert (cx, cy) == (F(10, 9), F(250, 189))
    density = cx*cy
    assert density == F(2500, 1701)
    gamma1 = density*F(1, 4)**3
    neighbours = F(1, 2)*6*F(1, 2)**2
    margin = (1-neighbours)*gamma1
    assert neighbours == F(3, 4) and gamma1 == F(625, 27216)
    assert margin == F(625, 108864)
    assert margin-F(1, 200) == F(2017, 2721600) > 0
    assert F(11, 4)-F(1, 200) == F(549, 200) == F('2.745')
    assert F(11, 4)-margin == F(298751, 108864)
    assert margin < F(1, 12) < F('0.098')
    print('Weak UM: 200 exact floor integrals; Cx >= 10/9, Cy >= 250/189;')
    print('gamma1 >= 625/27216; margin >= 625/108864 > 1/200; coefficient 549/200 = 2.745.')


def falling(n, h):
    out = 1
    for j in range(h):
        out *= n-j
    return out


def cp_sieve():
    cases = partner_cases = 0
    derangements = [1, 0]
    for n in range(2, 16):
        derangements.append((n-1)*(derangements[-1]+derangements[-2]))
    for k in range(16):
        ps = []
        for j in range(k+1):
            for r in range(j, k+1):
                value = sum(F((-1)**h*falling(r-j, h), factorial(h))
                            for h in range(k-j+1))
                assert value == int(r == j)
                cases += 1
            probability = sum(F((-1)**h, factorial(h)) for h in range(k-j+1))/factorial(j)
            assert probability == F(derangements[k-j], factorial(j)*factorial(k-j))
            ps.append(probability)
            if j:
                partners = sum(F((-1)**h, factorial(h)) for h in range(k-j+1))/factorial(j-1)
                assert partners == j*probability
                partner_cases += 1
        assert sum(ps) == 1
        if k:
            assert sum(j*p for j, p in enumerate(ps)) == 1
        if 2 <= k <= 7:
            fixed = Counter(sum(i == value for i, value in enumerate(perm))
                            for perm in permutations(range(k)))
            assert all(ps[j] == F(fixed[j], factorial(k)) for j in range(k+1))
    print(f'CP: {cases} sieve cases for 0 <= j <= r <= k <= 15; {partner_cases} size-biased identities;')
    print('rencontres and normalization checked independently, including exact permutations through k=7.')


def bt_arithmetic():
    for k in range(2, 1001):
        assert F(32*(k-1), 2)-12*(k-1) == 4*(k-1)
    # For n=10, geometric and differentiated geometric series, ratio 1/2.
    x, n = F(1, 2), 10
    tail = x**n*((n-1)/(1-x)+x/(1-x)**2)
    assert tail == F(5, 256)
    table = json.loads((ROOT/'slack/t221/standard_model.json').read_text())
    saving = F(0)
    for k in range(2, 10):
        descents = Counter(''.join(str(int(a > b)) for a, b in zip(perm, perm[1:]))
                           for perm in permutations(range(k)))
        assert sum(descents.values()) == factorial(k)
        saving += sum(count*F(str(min(table[bits])))/(factorial(k)*2**(k+2))
                      for bits, count in descents.items())
    assert saving == F(68350729, 123863040)
    assert 4-saving == F(427101431, 123863040)
    assert 4-saving-tail == F(424682231, 123863040)
    print('BT: 999 length checks; exact tail 5/256; table saving 68350729/123863040 (BS still required).')


def reference_block(row):
    """Build directly from xy=1 and reflection, independently of adjacent roots."""
    p = row['p']
    points = set()
    edges = set(row['run'][:-1])
    for a in range(1, p):
        b = pow(a, -1, p)
        if (a-b)**2*pow(4, -1, p) % p not in edges:
            continue
        for i in (0, 1):
            for j in (0, 1):
                x = (a+p//2) % p-p//2+i*p
                y = b+j*p
                points.update(((x, y), (p-x, y)))
    points = sorted(points)
    groups = defaultdict(list)
    for i, (x, y) in enumerate(points):
        for name, key in (('x', x), ('y', y), ('d', x-y), ('s', x+y)):
            groups[name, key].append(i)
    lines = [ids for _, ids in sorted(groups.items()) if len(ids) > 2]
    w = row['witness']
    if any(type(i) is not int for i in w):
        raise ValueError('noninteger reference witness')
    assert len(set(w)) == len(w) and all(0 <= i < len(points) for i in w)
    assert all(len(set(line) & set(w)) <= 2 for line in lines)
    dual = list(map(F, row['dual']))
    assert len(dual) == len(lines) and all(y >= 0 for y in dual)
    cover = [F(0) for _ in points]
    for y, line in zip(dual, lines):
        for i in line:
            cover[i] += y
    upper = 2*sum(dual)+sum(max(F(0), 1-c) for c in cover)
    assert str(upper) == row['upper']
    interval = (len(w), upper//1)
    assert list(interval) == row['beta_interval']
    return interval


def must_reject(action, message):
    try:
        action()
    except ValueError as error:
        assert message in str(error), (message, str(error))
    else:
        raise AssertionError('forged certificate accepted: '+message)


def verifier_regressions():
    path = ROOT/'bs_search/search_blocks.py'
    spec = spec_from_file_location('v122_verifier_under_test', path)
    verifier = module_from_spec(spec)
    spec.loader.exec_module(verifier)
    data = json.loads((ROOT/'bs_search/block_search.json').read_text())
    honest = next(r for r in data['rows'] if r['p'] == 11 and r['run'] == [3, 4, 5])
    assert reference_block(honest) == verifier.verify(honest) == (24, 24)
    forged = deepcopy(honest)
    forged.update(witness=[i+0.5 for i in range(64)], dual=['0']*len(honest['dual']),
                  upper='64', beta_interval=[64, 64])
    must_reject(lambda: reference_block(forged), 'noninteger')
    must_reject(lambda: verifier.verify(forged), 'witness indices must be integers')
    bad = deepcopy(honest)
    bad['witness'][0] = True
    must_reject(lambda: verifier.verify(bad), 'witness indices must be integers')
    bad = dict(honest, signature='10')
    must_reject(lambda: verifier.verify(bad), 'signature mismatch')
    bad = dict(honest, beta_interval=[24, 25])
    must_reject(lambda: verifier.verify(bad), 'beta interval mismatch')
    # Reject valid rows with incorrect dataset coverage or metadata.
    bad = dict(data, rows=[honest, honest])
    must_reject(lambda: verifier.verify_dataset(bad), 'duplicate block')
    bad = dict(data, rows=[honest])
    must_reject(lambda: verifier.verify_dataset(bad), 'incomplete block list')
    bad = dict(data, exact_optima=data['exact_optima']-1)
    must_reject(lambda: verifier.verify_dataset(bad), 'summary mismatch: exact_optima')
    print('Verifier: honest p=11 run [3,4,5] gives (24, 24); fractional forgery REJECTED;')
    print('bool indices, signature, interval, duplicate, missing block and wrong summary also REJECTED.')


if __name__ == '__main__':
    weak_margin()
    cp_sieve()
    bt_arithmetic()
    verifier_regressions()
    print('ALL v1.22 checks passed')
