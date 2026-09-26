"""verify_witness_2.py — a SECOND, independent check of an A280537 witness, sharing no code with verify_witness.py.
Method: for every triple of points compute the integer normal (cross product of two edge vectors); a zero normal is a
collinear triple (rejected); a fourth point whose offset from the triple has zero dot product with the normal lies on the
triple's plane (rejected). Everything else (distinctness, the cube bound, the expected count) is checked first.
usage: python3 verify_witness_2.py <n> <file> [<expected_m>]     python3 verify_witness_2.py --all <dir> [<dir> ...]     python3 verify_witness_2.py --selftest
Exit code 0 only when every checked witness is clean."""
import sys, os, re

def read_points(path):
    pts = []
    for raw in open(path, encoding="utf-8"):
        line = raw.split("#", 1)[0].strip()
        if not line: continue
        for m in re.finditer(r"\(\s*(-?\d+)\s*,\s*(-?\d+)\s*,\s*(-?\d+)\s*\)", line):
            pts.append((int(m.group(1)), int(m.group(2)), int(m.group(3))))
        if "(" not in line:
            f = line.split()
            if len(f) == 3 and all(re.fullmatch(r"-?\d+", x) for x in f): pts.append((int(f[0]), int(f[1]), int(f[2])))
    return pts

def verdict(n, pts, expected=None):
    """Returns (ok, message)."""
    m = len(pts)
    if m < 4: return False, "too few points (%d)" % m
    if expected is not None and m != expected: return False, "count %d differs from the expected %d" % (m, expected)
    if len({p for p in pts}) != m: return False, "points not distinct"
    if any(not (0 <= c < n) for p in pts for c in p): return False, "a point lies outside the %d-cube" % n
    for i in range(m):
        ax, ay, az = pts[i]
        for j in range(i + 1, m):
            ux, uy, uz = pts[j][0] - ax, pts[j][1] - ay, pts[j][2] - az
            for k in range(j + 1, m):
                vx, vy, vz = pts[k][0] - ax, pts[k][1] - ay, pts[k][2] - az
                nx, ny, nz = uy * vz - uz * vy, uz * vx - ux * vz, ux * vy - uy * vx
                if nx == 0 and ny == 0 and nz == 0: return False, "collinear triple %s %s %s" % (pts[i], pts[j], pts[k])
                for l in range(k + 1, m):
                    wx, wy, wz = pts[l][0] - ax, pts[l][1] - ay, pts[l][2] - az
                    if nx * wx + ny * wy + nz * wz == 0: return False, "coplanar quadruple %s %s %s %s" % (pts[i], pts[j], pts[k], pts[l])
    return True, "clean: %d points, no collinear triple, no coplanar quadruple" % m

def name_params(path):
    b = os.path.basename(path)
    m = re.search(r"n(\d+)_(\d+)", b)
    if m: return int(m.group(1)), int(m.group(2))
    m = re.search(r"n(\d+)", b)
    return (int(m.group(1)), None) if m else (None, None)

def run_all(dirs):
    allok = True; rows = []
    for d in dirs:
        for f in sorted(os.listdir(d)):
            if not f.endswith(".txt") or not (f.startswith("witness") or re.match(r"n\d+_\d+pts", f)): continue
            n, exp = name_params(f)
            if n is None: continue
            ok, msg = verdict(n, read_points(os.path.join(d, f)), exp)
            allok &= ok; rows.append((f, n, exp, ok, msg)); print("%-44s n=%-3d expected=%-4s %s  %s" % (f, n, exp, "OK " if ok else "FAIL", msg))
    print("%d witnesses, %d clean" % (len(rows), sum(1 for r in rows if r[3])))
    return allok

def selftest():
    here = os.path.dirname(os.path.abspath(__file__))
    good = read_points(os.path.join(here, "witness_n5.txt"))
    results = []
    results.append(("clean n=5 accepted", verdict(5, good, 13)[0] is True))
    results.append(("wrong count rejected", verdict(5, good, 12)[0] is False))
    results.append(("wrong cube rejected", verdict(4, good)[0] is False))
    planted = [(0, 0, 4), (1, 3, 4), (2, 1, 4), (4, 2, 4)] + [p for p in good if p[2] != 4][:9]
    results.append(("planted coplanar quadruple rejected", verdict(5, planted)[0] is False and "coplanar" in verdict(5, planted)[1]))
    coll = [(0, 0, 0), (1, 1, 1), (2, 2, 2), (0, 4, 1), (4, 0, 3)]
    results.append(("collinear triple rejected", "collinear" in verdict(5, coll)[1]))
    results.append(("duplicate rejected", verdict(5, good + [good[0]])[0] is False))
    for name, ok in results: print(("PASS " if ok else "FAIL ") + name)
    return all(ok for _, ok in results)

if __name__ == "__main__":
    a = sys.argv[1:]
    if not a: print(__doc__); sys.exit(2)
    if a[0] == "--selftest": sys.exit(0 if selftest() else 1)
    if a[0] == "--all": sys.exit(0 if run_all(a[1:]) else 1)
    n = int(a[0]); exp = int(a[2]) if len(a) > 2 else None
    ok, msg = verdict(n, read_points(a[1]), exp); print(("OK " if ok else "FAIL ") + msg); sys.exit(0 if ok else 1)
