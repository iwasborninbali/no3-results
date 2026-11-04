# Partition, independence, and verification

Counts are labeled subsets, with rotations and reflections counted separately.
The empty set is included. T(n,k) counts safe subsets and M(n,k) counts subsets
that admit no further grid point. The prior methods and provenance are retained
verbatim in `original_line_rows.c` and `original_determinant_check.c`.

The row program builds maximal grid lines by primitive integer directions,
maintains line occupancy, and chooses empty, singleton or pair patterns in each
row. The final row is completed analytically. Reflection in the vertical axis
is reduced at the first nonempty prefix row, exactly as in the prior program.
The determinant program builds constraints with integer determinants and
enumerates individual subsets by their selected point indices. It uses no
row completion and no symmetry weighting. Its source explicitly credits the
September `tri.c` adaptation, as the prior report does. `fixed_profiles.c` is
the prior supplementary symmetry audit, not the row enumerator.

Both new splitters partition by the first two coordinate rows, but generate
their frontiers independently. In the row program these are all surviving
row-pattern prefixes. In the determinant program a binary include/exclude
split decides each admissible prefix cell until no undecided prefix cell
remains. Covered cells cannot be included. A suffix search then counts all
extensions, including the empty suffix. Consequently every safe subset is
represented by exactly one frontier (with the row method's original reflection
weights accounting for discarded mirror prefixes). The splitter itself counts no subsets. This avoids
overlapping shallow-node corrections.

Frontiers are numbered in deterministic traversal order, and frontier i belongs
to shard i modulo S. Each shard recreates the small common frontier traversal
and expands only its assigned roots. Prefix line occupancies, effects, selected
points and reflection weights are preserved by ordinary recursive undo/state
rules. The two programs need not have the same frontier numbers or frontier
counts. Summing assigned frontier counts must equal the independently recorded
frontier count within each program. Common row-tree nodes above the cut are
charged only to shard 0, so the summed row-node profile must reproduce the old
unsharded node profile in validation.

Each program computes a direct addable-point ledger F(n,k). At a determinant
node it is popcount(full minus covered). In the row program it is the popcount
of the available cells after each zero-, one-, or two-point last-row completion,
with the original reflection weight. For a pair, the tail row is saturated;
the earlier available cells are intersected with the complements of both
effects. For a singleton, its own point and its saturated lines are removed
from the available grid. Thus F(n,k) is independently accumulated from actual
addability, rather than constructed from the target identity.

An incidence (S,p), where |S|=k and p is addable, corresponds uniquely to
(S union {p},p). Therefore F(n,k)=(k+1)T(n,k+1), with F(n,2n)=0. Maximality is
the absence of any addable point. The collector checks this ledger, both row
sums, M<=T, low-k binomial/collinear-triple formulas, all independent profile
cells, complete frontier coverage, determinant visits=sum T, row leaves equal
last-level nodes, and the supplied endpoints 380, 368, and 1135 at n=8,9,10.

Validation runs n=8 (32 shards per program) and n=9 (64 per program), comparing
all T and M cells with the previous exact outputs. The row leaf count and
every row-node count must also agree. A machine-readable `validation.json`
receipt is written only after both complete validations pass. The scheduler
launches n=10 only after that gate. Production uses 512 shards per program,
in a fixed randomized order, interleaving both methods across four slots.

For two adjacent prefix rows, every pair of legal row patterns is safe: a
collinear triple crossing rows would need two points in one horizontal row,
whose joining line cannot contain a point in the other row. Let
P=1+n+binomial(n,2). The determinant frontier therefore has exactly P^2 roots.
The row method has C reflection-canonical single-row patterns, including the
empty one, so its frontier has C+(C-1)P roots. At n=8,9,10 these independent
frontier predictions are respectively 1369/2116/3136 (determinant) and
761/1176/1711 (row). They are useful additional checks of the partition.

Successful shard results are atomically renamed from `.json.part`, then paired
with atomic receipts containing exit code, output SHA-256, build manifest hash,
command, PID and start/end UTC. `ledger.jsonl` journals starts and finishes;
individual verified receipts are authoritative. A restart skips verified
receipts. The checkpoint unit is a completed shard: an interrupted active
shard is rerun from its frontier, not resumed inside its recursion. `nohup`
protects the scheduler and its detached C processes against SSH loss. A flock
prevents a second live scheduler. Do not rebuild active binaries or start a
replacement scheduler while orphaned C processes are still alive.

`tree_estimate.c` retains the prior unbiased Knuth random-path estimator and
extends capacities to n=11 (121 cells fit unsigned __int128; 67 possible row
patterns fit the enlarged 80-entry buffers). Only Monte Carlo sampling is run
at n=11. Exact enumeration at n=11 is not launched. CPU-time rates are measured
separately from wall time, because other users' processes can contend for the
VM. Timing bands must include cost per node/leaf and machine uncertainty as
well as random-path sampling error.
