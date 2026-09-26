#!/usr/bin/env python3
"""Coverage check for the n=10 exhaustion of the cyclically invariant subspace (second solver, cyc3d_mine.c).
The first-orbit index runs over the NORB=340 orbits of n=10 (cells with x=y=z are 10 fixed orbits; (1000-10)/3 = 330 orbits of size 3).
The run was split by the index o of the first chosen orbit into residue classes; orbit 0 was split again by the second orbit index mod 8.
This script checks that the listed classes cover every index 0..339 exactly once, as recorded in coverage_n10_record.txt."""
NORB = 340
classes = [(r, 8) for r in (1, 4, 6)] + [(r, 16) for r in (2, 3, 5, 7, 8, 10, 11, 13, 15)] + [(r, 64) for r in (16, 32, 48)] + [(r, 256) for r in (64, 128, 192)] + [(256, 1024), (0, 1024)]
count = {o: 0 for o in range(NORB)}
for o in range(NORB):
    for r, m in classes:
        if o % m == r: count[o] += 1
missing = [o for o in count if count[o] == 0]; multiple = [o for o in count if count[o] > 1]
print("orbits", NORB, "classes", len(classes), "missing", missing, "covered more than once", multiple)
print("orbit 0 was split by the second orbit index into 8 residues mod 8: exhaustive by construction")
assert not missing and not multiple, "the partition does not cover the index set exactly once"
print("OK: exact partition")
