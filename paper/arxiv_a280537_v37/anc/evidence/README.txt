Evidence for the two exhaustion statements about the cyclically invariant subspace (maximum 23 at n=9, 26 at n=10)
and for the nineteen table configurations. Assembled 26 September 2026 for version 3.7 from the working repository
https://github.com/iwasborninbali/saturation (paths given as they stand there). MANIFEST.json carries SHA-256 of every file here.

ENUMERATORS (two implementations written without reading each other's code):
  no4_sym_exact.c   first solver (slack/targets/no4_sym_exact.c): full traversal of orbit unions of the cycle (x,y,z)->(y,z,x);
                    prunes: orbits in increasing index (each set once); p + 3r <= best (r orbits left, each adds at most 3 points);
                    an orbit is added only if it creates no collinear triple and no coplanar quadruple.  Build: cc -O3 -o no4_sym_exact no4_sym_exact.c;
                    run: ./no4_sym_exact n [seconds].
  cyc3d_mine.c      second solver (slack/targets/cyc3d_mine.c): the same subspace, independent code; prunes: admissibility of the orbit, and the
                    axis-plane capacity bound k + sum over layers of min(3 - occupied, available) <= best (each axis plane carries at most 3 points);
                    a branch is cut only against the current best, never against the unattainable target 3n (its own calibration found that error).
                    Build: cc -O3 -march=native -o cyc3d_mine cyc3d_mine.c; run: ./cyc3d_mine <n> <seconds> (sharding by first-orbit residue and, for
                    orbit 0, by the second orbit, as recorded in the logs).
  Prune validity: both bounds are upper bounds on what any completion of the branch can reach, so a branch cut cannot contain a configuration
  larger than the best already found; exhausting the tree with initial best B therefore proves that no configuration exceeds B.  It does not
  by itself show that B is attained: attainment is the verified witness (witnesses_table/, and the ancillary witness files).

RECORDS:
  record_first_solver_symmetry_2026-08-21.md      the first solver's record: n=9 maximum 23, 38 485 165 nodes; n=10 maximum 26, 496 667 762 nodes,
                                                  44 shards (43 within an hour); its own calibration reached 23 at n=9 but did not reach 26 at n=10
                                                  within its budget; the first solver states which of its assertions rest on which evidence.
  log_second_solver_n9_and_n10_first_attempts.txt  the second solver: calibration n=5..8 (13, 15, 18, 20 after fixing its own pruning error);
                                                  n=9 exhausted, maximum 23, 116 473 374 nodes, 916.6 s; the n=10 first attempts (threshold 25:
                                                  one shard of eight exhausted, seven reached 26; threshold 26: three shards of eight exhausted).
  interrupted_attempt_threshold25_shard0..7.txt   the eight early receipts of the interrupted threshold-25 attempt (ОБОРВАНО = interrupted); kept
                                                  to distinguish interrupted attempts from their completed replacements.
  log_second_solver_n10_completed.txt             the completed n=10 exhaustion: the exact partition of the first-orbit index (residues mod 8, 16, 64,
                                                  256, 1024; orbit 0 split by the second orbit into 8 shards), maximum 26 in every shard, no 27;
                                                  1 522 445 871 nodes, 8.93 core-hours; the calibration record (threshold 25 reached 26 in 7 of 8 shards).
  coverage_n10_record.txt                         the coverage table as written by the solver who closed each shard.
  coverage_check.py                               recomputes that the residue classes partition the 340 first-orbit indices exactly once (run: python3 coverage_check.py).

WHAT IS NOT HERE, stated plainly: per-shard terminal receipts (node count, seconds, status) for every shard of the completed runs were printed to
terminals and summarised in the logs above by group; they are not preserved as one file per shard for the second solver's residue groups nor for the
first solver's 44 shards.  The exhaustion statements in the note therefore rest on the recorded run reports of two independent implementations,
not on a receipt per shard.  No large exhaustion was re-run for this version; the n=5 and n=6 calibrations of cyc3d_mine.c were reproduced by the
reviewer on 26 September 2026 (4 494 and 64 444 nodes).

WITNESSES (witnesses_table/): the nineteen table configurations, one file per size n = 9..25, 27, 29 (largest recorded configuration per size in
certs/a280537_first_solver), each re-verified on 26 September 2026 with anc/verify_witness.py (exit 0, zero coplanar quadruples); see MANIFEST.json.
