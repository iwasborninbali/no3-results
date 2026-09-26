"""Independent exact finite checks for v1.21; standard library only.

Run: python3 verify_v121.py
No imports from the other verification programs and no solver or network.
Finite checks do not prove an asymptotic law or any named hypothesis.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations, product
from math import gcd


def line(a, b):
    dx, dy = b[0] - a[0], b[1] - a[1]
    d = gcd(dx, dy)
    A, B = dy // d, -dx // d
    if A < 0 or (A == 0 and B < 0):
        A, B = -A, -B
    return A, B, A * a[0] + B * a[1]


def rich_lines(points):
    lines = defaultdict(set)
    for i, j in combinations(range(len(points)), 2):
        lines[line(points[i], points[j])].update((i, j))
    return [v for v in lines.values() if len(v) >= 3]


def hyperbola(p, c, x0, y0, n):
    return [(x, y) for x in range(x0, x0 + n)
            for y in range(y0, y0 + n) if x * y % p == c]


def exact_maximum(points):
    """Split the actual rich-line incidence graph, then exhaust each component."""
    lines = rich_lines(points)
    parent = list(range(len(points)))

    def root(i):
        while parent[i] != i:
            i = parent[i]
        return i

    for indices in lines:
        r = root(min(indices))
        for i in indices:
            parent[root(i)] = r
    components = defaultdict(list)
    for i in range(len(points)):
        components[root(i)].append(i)
    witness = []
    for indices in components.values():
        lookup = {i: j for j, i in enumerate(indices)}
        masks = [sum(1 << lookup[i] for i in v) for v in lines
                 if min(v) in lookup]
        for size in range(len(indices), -1, -1):
            found = None
            for chosen in combinations(range(len(indices)), size):
                mask = sum(1 << j for j in chosen)
                if all((mask & v).bit_count() <= 2 for v in masks):
                    found = [points[indices[j]] for j in chosen]
                    break
            if found is not None:
                witness.extend(found)
                break
    assert not rich_lines(witness)
    return witness


def check_windows():
    small = hyperbola(11, 1, 0, 0, 22)
    large = hyperbola(11, 1, 0, 0, 23)
    assert small == large and len(small) == 40
    assert len(exact_maximum(large)) == 22 < 30
    print('F1: p=11, c=1: [0,23)^2 and [0,22)^2 have the same 40 points; exact maximum 22 < 30.')
    cases = enlargements = 0
    for p in (3, 5, 7, 11, 13, 17, 19):
        for c in range(1, p):
            h = (p - 1) // 2
            base = hyperbola(p, c, -h, 0, 2 * p)
            witness = exact_maximum(base)
            assert len(witness) == 3 * (p - 1)
            # Both anchored squares and squares extended on all four sides.
            for left, down, extra in ((0, 0, 1), (0, 0, p), (1, 2, 3)):
                enlarged = set(hyperbola(p, c, -h-left, -down, 2*p+extra))
                assert set(base) <= enlarged and set(witness) <= enlarged
                enlargements += 1
            cases += 1
    print(f'F1: {cases} exact HJSW maxima, all nonzero c at primes 3..19; lawful witnesses retained in {enlargements} containing squares.')


def cubic_counts(p, a, x0, y0):
    base = {x: (x0 + (x-x0) % p, y0 + (a*x**3-y0) % p) for x in range(p)}
    points = {(r+d*p, s+e*p) for r, s in base.values() for d, e in product((0, 1), repeat=2)}
    fibres, weighted, triples, exceptional = {}, {}, {}, {}
    triple_member, split_member = {}, {}
    A, S = {}, {}
    for slope in (1, -1):
        fibres[slope] = defaultdict(list)
        for x in range(p):
            fibres[slope][(a*x**3-slope*x) % p].append(x)
        actual = defaultdict(set)
        for X, Y in points:
            actual[Y-slope*X].add((X, Y))
        for intercept, pts in actual.items():
            if len(pts) >= 4:
                key = slope, intercept
                weighted[key] = pts
                target = triples if len(fibres[slope][intercept % p]) == 3 else exceptional
                target[key] = pts
        triple_member[slope], split_member[slope] = set(), set()
        A[slope] = S[slope] = 0
        for roots in fibres[slope].values():
            if len(roots) != 3:
                continue
            triple_member[slope].update(roots)
            centres = {base[x][1]-slope*base[x][0] for x in roots}
            assert len(centres) in (1, 2)
            split = len(centres) == 2
            A[slope] += not split
            S[slope] += split
            if split:
                split_member[slope].update(roots)
    L0 = sum(A[s]+2*S[s] for s in (1, -1))
    U0 = sum((x not in triple_member[1]) * (2-(x in split_member[-1]))
             + (x not in triple_member[-1]) * (2-(x in split_member[1])) for x in range(p))
    triple_covered = set().union(*triples.values())
    extra_covered = set().union(*exceptional.values()) - triple_covered
    direct_covered = set().union(*weighted.values())
    assert L0 == len(triples) and U0 == len(points-triple_covered)
    # Exact exceptional-fibre corrections underlying the printed O(1)'s.
    L, U = L0 + len(exceptional), U0 - len(extra_covered)
    assert L == len(weighted) and U == len(points-direct_covered)
    assert len(exceptional) <= 4 and len(extra_covered) <= 16
    return L, L0, U, U0, A, S


def check_cubics():
    case = cubic_counts(23, 1, 0, 0)
    assert case[:4] == (13, 11, 36, 42)
    print('F2: p=23, a=1, B=[0,46)^2: L4=11+2=13; U=42-6=36.')
    case11 = cubic_counts(11, 1, 0, 0)
    assert (case11[4][1], case11[5][1]) == (1, 0)
    print('F2: p=11 positive slope: same=1, split=0; finite split proportion is not 1/2.')
    cases = 0
    for p in (5, 11, 17, 23, 29, 41, 47, 59):
        for a in range(1, p):
            for x0, y0 in ((0, 0), (-(p//2), 0), (1, 2), (p//3, -p//2)):
                cubic_counts(p, a, x0, y0)
                cases += 1
    print(f'F2: corrected exact L4 and U formulas match direct enumeration in {cases} cases at eight primes, every a and four boxes; corrections bounded by 4 lines and 16 points.')


def centred(x, p):
    return (x + p//2) % p - p//2


def check_signs():
    assert (centred(-6, 11), (-2) % 11) == (5, 9)
    assert 2-6 == 5-9 and 2*5 > 0
    print('F4: p=11 base copies (2,6),(5,9): common centre -4; first coordinates have the same sign.')
    pairs = torus_points = 0
    for p in (5, 7, 11, 13, 17, 19, 23, 29, 31):
        for x in range(1, p):
            X, Y = centred(x, p), pow(x, -1, p)
            Xs, Ys = centred(-Y, p), (-X) % p
            shared = X-Y == Xs-Ys
            assert shared == (X*Xs > 0) == (X*centred(Y, p) < 0)
            pairs += 1
        # Exhaust the discrete centred torus with u1-u2+u3+u4=0 mod p.
        # The signed permutation is an involution of determinant +/-1,
        # hence also preserves Haar measure on the continuous torus.
        for u1, u2, u3 in product(range(-p//2+1, p//2+1), repeat=3):
            u4 = centred(-u1+u2-u3, p)
            v = (u3, -u4, u1, -u2)
            assert (v[0]-v[1]+v[2]+v[3]) % p == 0
            assert (v[2], -v[3], v[0], -v[1]) == (u1, u2, u3, u4)
            assert (u1*u2 < 0) == (v[2]*v[3] > 0)
            assert (u3*u4 > 0) == (v[0]*v[1] < 0)
            torus_points += 1
    assert Fraction(11, 3)-Fraction(7, 96) == Fraction(115, 32)
    print(f'F4: {pairs} base-pair checks and {torus_points} torus points at nine primes; corrected symmetry preserves relation and swaps sharing events; 115/32 unchanged.')


if __name__ == '__main__':
    check_windows()
    check_cubics()
    check_signs()
    print('ALL v1.21 checks passed')
