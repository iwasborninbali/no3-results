# Exact count profiles of no-three-in-line subsets: two independent sharded programs

These programs computed the exact rows n ≤ 9 in `../2026-11-03/`. The exact n = 10 row is running now. Code: MIT; data: CC BY 4.0.

- **Counted objects.** T(n,k) is the number of k-subsets of the n×n grid with no three collinear points. M(n,k) is the number of such subsets to which no grid point can be added. Subsets are labelled: rotations and reflections are counted separately, and the empty set is included.
- **Two programs**, written independently (details in `method.md`):
  - `line_rows.c` is a row-by-row search over row patterns (empty, singleton, pair), with line-occupancy bookkeeping, analytic completion of the last row, and a vertical-reflection reduction.
  - `determinant_check.c` checks every triple by integer determinants and uses no symmetry weighting.
  - Both partition the work by the first two rows into deterministic frontiers; frontier i belongs to shard i mod S. Every safe subset is counted in exactly one shard.
- **Validation.** Both programs agree on every row for n ≤ 9 (references in `reference/`), and the 2n-point count matches A000755.
- **Run one shard:**
  - `./build.sh`
  - `./line_rows N --shard i --shards S --split-rows R`
  - `./determinant_check N i S R` (N ≤ 11)
  - `pipeline.py`, `collect.py` and `audit.py` are our four-worker queue, the aggregator and the receipt checker.
- **Cost estimates.** From `tree_estimate.c` (sampled tree sizes) and measured n = 10 throughput on one VM core. These are planning bands, not confidence intervals.

| n | both programs, core-hours (expected) | planning band |
|---:|---:|---:|
| 10 | 114 | 83–164 |
| 11 | 5,626 | 3,371–8,917 |

- **Estimated n = 11 total:** about 3.15·10¹⁴ safe subsets (sampling SE 1.7%). This is an estimate, not a sequence term.
