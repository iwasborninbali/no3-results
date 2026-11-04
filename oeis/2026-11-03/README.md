# Exact rows n = 1..9 for A398172, A398184, A398580 (computed 3 November 2026)

No-three-in-line subsets of the n×n grid: A398172 counts all safe subsets, A398184 the maximal ones
(by size in `maximal_by_size.txt`), A398580 is the triangle T(n,k) of safe k-subsets.

- n = 8 was already in the OEIS (credited to Sean A. Irvine); our value agrees.
- **n = 9 is new**: 167,892,639,418 safe subsets and 1,861,878,186 maximal ones; the full row of
  A398580 for n = 9 is in `DATA_extensions.txt` and `b398580.txt`.
- Two independent programs agree on every row (`programs.txt`; provenance in `provenance.txt`).
- Not yet submitted to the OEIS. The exact n = 10 row is being computed.
