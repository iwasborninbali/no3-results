Evidence for the two exhaustion statements about the cyclically invariant subspace (maximum 23 at n=9, 26 at n=10)
and for the nineteen table configurations. Assembled 26 September 2026 for versions 3.7 and 3.8 from the working repository
https://github.com/iwasborninbali/saturation (paths given as they stand there). MANIFEST.json carries SHA-256 of every file here.

ENUMERATORS. Each solver states that it wrote its program without reading the other's code; that statement is the solvers' own, recorded in their reports, not measured by this package.
  First solver, three files:
    no4_sym_exact.c      full traversal of orbit unions of the cycle (x,y,z)->(y,z,x) without an external incumbent; prunes: orbits in increasing index;
                         p + 3r <= best; admissibility (no collinear triple, no coplanar quadruple).  Build: cc -O3 -o no4_sym_exact no4_sym_exact.c;
                         run: ./no4_sym_exact n cyc3 [seconds]  (argument 2 is the group; any other value selects the half-turn group rot2, a
                         different problem).  The first solver's record reports a calibration table n = 5..8 for its full traversal; this shipped
                         source reproduces the record's node counts at n = 5 (13 in 5 366 nodes) and n = 6 (15 in 71 838) but NOT at n = 7
                         (876 026 nodes against the record's 323 856); at n = 8 it exhausts cyc3 with maximum 20 in 14 044 102 nodes (26 September 2026, 7.8 min, no time limit hit)
                         against the record's 4 989 036; the proof programs below give 224 501 and
                         196 683 nodes at n = 7 with incumbents 17 and 18.  No shipped program reproduces the record's counts from n = 7
                         up; the program version behind the record's table is not in the repository as shipped.
    no4_sym_fastproof.c  the proof program: the list of live orbits is passed down, bound p + 3*|live|; the incumbent is supplied from outside and
    no4_sym_cap.c        the traversal checks only branches that could exceed it; two-level sharding.  Run: ./no4_sym_cap n incumbent [seconds]
                         [shard nshard [shard2 nshard2]].  no4_sym_cap.c adds the echo-of-input safeguard (the initial incumbent printed beside the
                         answer) after the reading error described in the record, and removes the direction-filter machinery of the earlier
                         file; the two files are the candidate lineage matching the recorded description of the first solver's n = 9 and n = 10
                         runs (the record's account of the pruning and of the 44 shards with a 12-way second-level split matches this interface);
                         neither source was execution-audited beyond the small cases stated below.  WHAT IS NOT BOUND: the exact version of the program used for each historical shard and the
                         per-shard invocations were not recorded; the association of these sources with those runs rests on the record's
                         description, not on a receipt.
  Second solver, one file:
    cyc3d_mine.c         the same subspace, independent code; prunes: admissibility of the orbit, and the axis-plane capacity bound k + sum over
                         layers of min(3 - occupied, available) <= best; a branch is cut only against the current best (never against the
                         unattainable target 3n; its own calibration found that error).  Build: cc -O3 -march=native -o cyc3d_mine cyc3d_mine.c;
                         run: ./cyc3d_mine n seconds [target] [shard nshard] [best0] [shard2 nshard2]; the shipped source is the file as it stands after the work: the log records that the second-level sharding and the report line were added or repaired during the n = 10 runs, so this file is not bound as the exact source of every completed shard either; the n = 10 partition was run with best0 = 26
                         and the residue classes of coverage_n10_record.txt (first-orbit residues mod 8, 16, 64, 256, 1024; orbit 0 split by the
                         second orbit mod 8); the per-shard invocations were not preserved as files.
  Prune validity: both bounds are upper bounds on what any completion of the branch can reach, so a branch cut cannot contain a configuration
  larger than the best already found; exhausting the tree with initial incumbent B therefore proves that no configuration exceeds B.  It does not
  by itself show that B is attained: attainment is the verified witness (witnesses_table/, and the ancillary witness files).

RECORDS:
  record_first_solver_symmetry_2026-08-21.md      the first solver's record: n=9 maximum 23, 38 485 165 nodes; n=10 maximum 26, 496 667 762 nodes,
                                                  44 shards (43 within an hour); its own calibration reached 23 at n=9 but did not reach 26 at n=10
                                                  within its budget; the first solver states which of its assertions rest on which evidence.
  log_second_solver_n9_and_n10_first_attempts.txt  the second solver: calibration n=5..8 (13, 15, 18, 20 after fixing its own pruning error);
                                                  n=9 exhausted, maximum 23, 116 473 374 nodes, 916.6 s; the n=10 first attempts (threshold 25:
                                                  one shard of eight exhausted, seven reached 26; threshold 26: three shards of eight exhausted).
  interrupted_attempt_threshold25_shard0..7.txt   eight receipts of a LATER, five-minute rerun of the threshold-25 shards (about 300 s and 12.6–17 million
                                                  nodes each, all interrupted, none reaching 26; they carry the second-level field and the echo warning
                                                  that were added after the completed run).  They are NOT the receipts of the 3000-second attempt
                                                  described in the log, and they give no support to the «seven of eight shards reached 26» calibration,
                                                  which rests on the log text alone.  Kept as what they are.
  log_second_solver_n10_completed.txt             the completed n=10 exhaustion: the exact partition of the first-orbit index (residues mod 8, 16, 64,
                                                  256, 1024; orbit 0 split by the second orbit into 8 shards), no shard exceeded the initial incumbent 26 (attainment of 26 is certified separately by the witness; a run seeded with 26 reports only that nothing exceeded it), no 27;
                                                  1 522 445 871 nodes, 8.93 core-hours; the calibration record (threshold 25 reached 26 in 7 of 8 shards).
  coverage_n10_record.txt                         the coverage table as written by the solver who closed each shard.
  coverage_check.py                               recomputes that the residue classes partition the 340 first-orbit indices exactly once (run: python3 coverage_check.py).

WHAT IS NOT HERE, stated plainly: per-shard terminal receipts (node count, seconds, status) for every shard of the completed runs were printed to
terminals and summarised in the logs above by group; they are not preserved as one file per shard for the second solver's residue groups nor for the
first solver's 44 shards.  The exhaustion statements in the note therefore rest on the recorded run reports of two independent implementations,
not on a receipt per shard.  The n = 10 and n = 9 exhaustions of cyc3d_mine.c WERE re-run for this version (26 September 2026) as 64 and 8 receipted shards, see n10_rerun/ and n9_rerun/ below; the n=5 and n=6 calibrations of cyc3d_mine.c were reproduced by the
reviewer on 26 September 2026 (4 494 and 64 444 nodes).

WITNESS HEADERS: the historical header lines of several witness files (n = 15, 18, 25, 27, 29 in witnesses_table/ and witness_n27_56_record.txt) say «no published data for this n» or that the sequence stops at a(8); those remarks are the solver's belief at the time and are superseded by Section 2 of the note (the contest report and the OEIS coordinate file carry prior configurations); the files are kept byte-identical for provenance.

WITNESSES (witnesses_table/): the nineteen table configurations, one file per size n = 9..25, 27, 29 (largest recorded configuration per size in
certs/a280537_first_solver), each re-verified on 26 September 2026 with anc/verify_witness.py WITH the expected point count as the third argument (exit 0, zero coplanar quadruples, count bound); see MANIFEST.json.

Change in version 3.8 (26 September 2026, after the reviewer's third pass): the first solver's proof-program lineage (no4_sym_fastproof.c, no4_sym_cap.c) added beside its calibration program; the run recipes corrected (the group argument of no4_sym_exact; the full argument list of cyc3d_mine); what is and is not bound stated per program; «no shard exceeded the initial incumbent 26» in place of «maximum 26 in every shard»; the independence statement attributed to the solvers.

Change in version 3.9 (26 September 2026, after the reviewer's fourth pass): two precision edits in this README (candidate lineage; the n = 5 reproduction stated as the only rerun of the first solver's program). No other file changed.

Change in version 4.0 (26 September 2026, after a fresh independent read): the eight receipts relabelled as a later rerun; the shipped first-solver source stated not to reproduce the record from n = 7 up; the historical witness headers noted as superseded; every witness re-verified with the point count bound.

Change in version 4.1 (26 September 2026, after the fifth returning-reviewer pass): the n = 8 count of no4_sym_exact.c remeasured (maximum 20 reproduced, node count 14 044 102 against the record's 4 989 036); the second solver's source stated as not bound to every completed shard; nothing else here changed.

n10_rerun/ (added in version 4.2): the shipped cyc3d_mine.c (byte-identical copy inside; SHA-256 of source and binary in hashes.txt) compiled with gcc -O2 on an
  8-core Apple laptop and run on 26 September 2026 (started 2026-09-26T10:33:10.613848, six processes in parallel under caffeinate) as 64 processes
  ./cyc3d_mine 10 400000 27 s 8 26 k 8  for s, k in 0..7 (jobs.txt): first chosen orbit index modulo 8 by second chosen orbit index modulo 8, each started
  with the incumbent 26 and the target 27, no time limit reached.  One receipt per shard (the program's stdout as written): every one reports
  "ИСЧЕРПАНО — НЕ ПРЕВЗОШЁЛ НАЧАЛЬНОГО" (exhausted; did not exceed the initial incumbent).  coverage_n10_rerun.py checks the 64-shard partition,
  the statuses and the partition line of every receipt and sums them (summary.json): 1,522,448,281 nodes, 27,386 s of summed shard wall time (7.61 process-hours: the program records each process's elapsed wall time with CLOCK_MONOTONIC; one process per shard, six in parallel, so this is not a CPU-clock measurement), longest shard 1666 s.
  What this certifies: with the incumbent 26 no shard found 27; attainment of 26 is certified separately by the witness.  What it does not
  certify: the historical production runs of 21-22 August (their reports remain as recorded above); the n = 9 exhaustion was not re-run.
Change in version 4.3 (26 September 2026): the rerun's time labelled as summed shard wall time (process-hours), not core-hours; coverage script keys renamed accordingly; summary.json regenerated.

n9_rerun/ (added in version 4.3): the same shipped cyc3d_mine.c (copy inside; SHA-256 of source and binary in hashes.txt) run on 26 September 2026 (started 2026-09-26T12:09:43.046148,
  four processes in parallel under caffeinate) as 8 processes  ./cyc3d_mine 9 100000 24 s 8 23  for s in 0..7 (jobs.txt): first chosen orbit index modulo 8,
  each started with the incumbent 23 and the target 24, no time limit reached.  One receipt per shard: every one reports "ИСЧЕРПАНО — НЕ ПРЕВЗОШЁЛ
  НАЧАЛЬНОГО".  coverage_n9_rerun.py checks the partition, the statuses and sums them (summary.json): 115,838,153 nodes, 1,089 s of summed shard wall time
  (0.30 process-hours), longest shard 396 s.  Certifies that with the incumbent 23 no shard found 24; attainment of 23 is the witness's.
greedy_budget/ (added in version 4.3): greedy_budget.c (copy inside; hashes.txt), the fixed-budget greedy measurement of Section 7: one seed, one core,
  15 s of uniform random greedy restarts (the cell drawn uniformly among the alive cells), 8 seeds (1..8) for each of n = 5, 6, 7, 8 with targets 13, 16, 18, 20
  (jobs.txt; four processes in parallel; started 2026-09-26T12:15:26.021500); one receipt per seed with the restart count, the best size and whether the target was reached.
  Fractions reached: n = 5 7/8, n = 6 0/8, n = 7 0/8, n = 8 0/8.  The August journal measurement used a faster implementation (roughly 160,000 restarts per seed at n = 6) and gave 8/8, 0/8, 0/8, 0/8.
