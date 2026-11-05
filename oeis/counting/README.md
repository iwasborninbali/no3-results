# Exact count profiles of no-three-in-line subsets: two independent sharded programs

These programs computed the exact rows n ≤ 10. The n = 10 profile, every shard receipt and a reproduction guide are in [`results/n10/`](results/n10/). Code: MIT; data: CC BY 4.0.

- **Counted objects.** T(n,k) is the number of k-subsets of the n×n grid with no three collinear points. M(n,k) is the number of such subsets to which no grid point can be added. Subsets are labelled: rotations and reflections are counted separately, and the empty set is included.
- **Two programs**, written independently (details in `method.md`):
  - `line_rows.c` is a row-by-row search over row patterns (empty, singleton, pair), with line-occupancy bookkeeping, analytic completion of the last row, and a vertical-reflection reduction.
  - `determinant_check.c` checks every triple by integer determinants and uses no symmetry weighting.
  - Both partition the work by the first two rows into deterministic frontiers; frontier i belongs to shard i mod S. Every safe subset is counted in exactly one shard.
- **Validation.** Both programs agree on every profile, maximal-profile and freedom-ledger cell through n = 10; n ≤ 9 also match `reference/`. The 2n-point count matches A000755. For n = 10 the two programs each completed 512/512 shards and agreed on 7,287,023,194,031 safe subsets and 56,412,888,628 maximal sets. The known endpoint is 1,135.
- **Run one shard:**
  - `./build.sh`
  - `./line_rows N --shard i --shards S --split-rows R`
  - `./determinant_check N i S R` (N ≤ 11)
  - `pipeline.py`, `collect.py` and `audit.py` are our four-worker queue, the aggregator and the receipt checker.
- **Cost estimate for n = 11.** From `tree_estimate.c` (sampled tree sizes) and measured n = 10 throughput. The estimate of 5,626 core-hours (planning band 3,371–8,917) is not a statistical confidence interval. The completed n = 10 run used 134,324 row CPU-seconds and 238,724 determinant CPU-seconds, about 103.6 core-hours total; the previous n = 10 forecast was 114 core-hours (planning band 83–164).

- **Estimated n = 11 total:** about 3.15·10¹⁴ safe subsets (sampling SE 1.7%). This is an estimate, not a sequence term.
