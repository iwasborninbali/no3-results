Ancillary files for "Nineteen certified configurations, eighteen independent bounds for the no-four-coplanar problem in the cube, and what they do not establish" (version 4.2, 26 September 2026; manuscript revised after the sixth returning-reviewer pass and a fresh independent read; ancillary files as completed in 3.5; Zenodo concept doi:10.5281/zenodo.22023079).

verify_witness_2.py -- the SECOND, independent check, sharing no code with verify_witness.py: for every triple the integer normal (cross
                       product); a zero normal is a collinear triple; a fourth point with zero dot product lies on the triple's plane; distinctness,
                       range and the expected count are checked first.  usage: python3 verify_witness_2.py <n> <file> <expected_m>;
                       python3 verify_witness_2.py --all <dir> [<dir> ...] sweeps witness files; --selftest plants a coplanar quadruple and a collinear triple.
verify_witness.py   -- checks a configuration file: all C(m,4) quadruples by exact 3x3 determinants (0 coplanar expected), distinctness, range.
                       usage: python3 verify_witness.py <n> <file> <expected_m>   (the third argument binds the point count; without it only the geometry is checked)   self-test: python3 verify_witness.py --selftest (uses witness_n5.txt)
witness_n5.txt      -- the self-test fixture: a clean 13-point configuration at n=5 into which the self-test plants coplanar quadruples.

The eleven inequivalent optimal or best-known configurations of Section 9, one file each (header lines "#" give provenance; then one point "x y z" per line):
  n=7,  18 points, three classes:  witness_n7_18_first_solver.txt, witness_n7_18_c03_ord2_strata.txt, witness_n7_18_c06_ord3_strata.txt
  n=8,  20 points, three classes:  witness_n8_20_first_solver.txt, witness_n8_20_c03_ord2_strata.txt, witness_n8_20_c06_ord3_strata.txt
  n=9,  23 points, three classes:  witness_n9_23_first_solver.txt, witness_n9_23_c06_ord3_long.txt, witness_n9_23_c06_ord3_strata.txt
  n=11, 28 points, two classes:    witness_n11_28_first_solver.txt, witness_n11_28_c06_ord3_long.txt

The four record lower bounds stated in the manuscript (a(12) >= 31, a(21) >= 47, a(22) >= 49, a(27) >= 56), one witness each:
  witness_n12_31_record.txt, witness_n21_47_record.txt, witness_n22_49_record.txt, witness_n27_56_record.txt

Every file above was re-checked on 26 September 2026 with verify_witness.py (exit 0, zero coplanar quadruples) and with verify_witness_2.py (--all over anc/ and evidence/witnesses_table/: 35 witnesses, 35 clean). The complete table of certified lower bounds (n = 9..29) and all other configurations are in the Zenodo record and in https://github.com/iwasborninbali/saturation (certs/a280537, certs/a280537_first_solver).
Change from version 3.4: the four first-class files and the four record witnesses were absent from the package although named in the README and the manuscript; the self-test fixture was absent. Added; nothing else changed.

Change in version 3.6 (26 September 2026): manuscript text revised after the first adversarial review (prior-art baseline corrected: the OEIS coordinate file has configurations at n = 14, 15, 18, our n = 18 is below 43; the correlation mechanism withdrawn; finite-search observations no longer stated as complexity or causal claims; the planar enrichment no longer asserted for the cube; rigidity and exchange statements made precise; small accuracy fixes). Ancillary files unchanged.

Change in version 3.7 (26 September 2026): evidence/ added (both enumerators, the recorded run reports of the n = 9 and n = 10 exhaustions, the n = 10 shard coverage and its check script, the eight interrupted early receipts, the nineteen table witnesses re-verified, MANIFEST.json with SHA-256 of every file); the abstract's exclusivity clause deleted and the exhaustion statements phrased as resting on recorded reports; «tie, our witness supplied» in the table; one sentence on what the reported search settles.

Change in version 3.8 (26 September 2026): evidence/ completed after the reviewer's third pass (see evidence/README.txt); two sentences of the text now say that the first solver's production program version is not bound by the records.

Change in version 3.9 (26 September 2026): two precision edits in evidence/README.txt; the date line.

Change in version 4.0 (26 September 2026): Section 2 corrected against the contest's final report (point sets published for the prime sizes) and the full OEIS coordinate file; table verdicts named by source; the two heuristics of Section 6 defined; the plane count of Section 9 defined; the OEIS entry's author corrected in the bibliography; Section 4 cited for verification; evidence/ updated (see evidence/README.txt).

Change in version 4.1 (26 September 2026): the abstract distinguishes the already published n = 12 from the three further improvements; the comparison table dated; Section 6 restated from the 21 August journal with its conventions and the full plane family; Section 9 states the generator's operational plane filter and its sufficiency; the provenance caveat extended to both solvers; usage line shows the count argument.

Change in version 4.2 (26 September 2026): verify_witness_2.py shipped (the second program of Section 4); the OEIS-file attributions stated as the file states them and the coincidences with our sets qualified as up to a cube symmetry; the contest report described by its solutions section; the n = 11 pair added to Section 9 (stabilisers 3 and 3, overlap 4 of 28, both rigid) so that the eleven files listed above are all stated in the text; the vacuous stratum sentence removed; Section 6 first crossing restricted to m >= 4 and the "leaning" sentence replaced by the two signed deviation sequences; the calibration sentence names the n = 9 stratum run (FEASIBLE, bound 27) beside n = 10; the bibliography attributes the references to the entries that carry them; the author's unlinked OEIS file of 23 August 2026 named and superseded.
