# no3-results — the results of an AI-driven research programme on the no-three-in-line problem

Curated, read-only entry point: the papers, the OEIS contributions, the witness configurations and the independent
verifiers, split off from the working journal repository
[iwasborninbali/saturation](https://github.com/iwasborninbali/saturation) on 10 September 2026. Nothing here is
new relative to that repository and the Zenodo records; this is the shelf, not the workshop.

**Provenance.** The searching, the verification and the drafting were carried out by AI agents (Anthropic Claude)
under the direction of Aleksei Kudriashov (Alex Komang), who posed the questions, chose what to compute, decided
what to claim and is responsible for the content. Every witness was checked by a second program that shares no
code with the program that found it; every number in every paper traces to a journal file in the working
repository.

## Papers (each concept DOI resolves to the latest version; PDF, TeX and data in every Zenodo record)

| paper | version | sources / PDF here | concept DOI |
|---|---|---|---|
| Exact values and certified lower bounds for the no-three-in-line problem in the cube | 1.5 | `paper/arxiv_no3_3d_v15/`, `paper/no3_3d_note.pdf` | [10.5281/zenodo.22019279](https://doi.org/10.5281/zenodo.22019279) |
| Certified configurations and bounds for the no-four-coplanar problem in the cube (A280537) | 4.1 (26 Sep 2026: after six review passes; two definitions repaired) | `paper/arxiv_a280537_v41/`, `paper/a280537_note.pdf` (PDF of 3.4) |
| 4.2 (26 Sep 2026: after the sixth pass and a fresh independent read; second verifier shipped; n=10 exhaustion re-run with a receipt per shard) | `paper/arxiv_a280537_v42/`, `paper/a280537_note.pdf` (PDF of 3.4) |
| 4.3 (26 Sep 2026: after the returning reviewer's delta of 4.2 and a second fresh read; wall-time label) | `paper/arxiv_a280537_v43/`, `paper/a280537_note.pdf` (PDF of 3.4) |
| 4.4 (26 Sep 2026: two editorial corrections after the reviewer's delta of 4.3; the version to submit) | `paper/arxiv_a280537_v44/`, `paper/a280537_note.pdf` (PDF of 3.4) | [10.5281/zenodo.22023079](https://doi.org/10.5281/zenodo.22023079) |
| Extremal no-three-in-line subsets of a modular hyperbola in the Hall–Jackson–Sudbery–Wild window | 1.19 (26 Sep 2026: one remark made conditional, tag reconciled) | `paper/arxiv_hjsw_window_v119/`, `paper/hjsw_window.pdf` | [10.5281/zenodo.22063297](https://doi.org/10.5281/zenodo.22063297) |
| 1.20 (26 Sep 2026: status corrections after three reads of 1.19: the unproved steps are five named hypotheses (BS, BT, CP, PC, UM), Lemma FE corrected, empirical sentences relabelled, runnable ancillary bundle; superseded by 1.21, not released) | `paper/arxiv_hjsw_window_v120/` (PDF inside) | |
| 1.21 (26 Sep 2026: after three reads of 1.20: one remark restricted to windows containing the HJSW window; proof corrections (exceptional fibres in the cubic proof, comparison rates weakened to o(p) with every leading constant unchanged, signs in the closure and seven-group arguments); independent finite checks in `anc/verify_v121.py`; passed its three reads, not yet released) | `paper/arxiv_hjsw_window_v121/` (PDF inside) | |
| 1.22 (26 Sep 2026: PC, BT and CP (under its structural hypotheses) proved, and a weaker uniform margin; the permutation-cubic bound (2.745+o(1))p is unconditional for p ≡ 2 (mod 3), a ≠ 0 and half-open 2p×2p boxes; UM, the coefficient 2.652, G3 and BS remain open; exact finite block certificates for p ≤ 503 and exact checks in `anc/verify_v122.py`; portable paths in the ancillary bundle; passed its three reads, not yet released) | `paper/arxiv_hjsw_window_v122/` (PDF inside) | |
| Balanced orbit defects in half-turn-symmetric no-three-in-line configurations | 1.3 | `paper/arxiv_no3inline_defects_v13/`, `paper/no3inline_defects.pdf` | [10.5281/zenodo.22063287](https://doi.org/10.5281/zenodo.22063287) |
| The error of the Guy–Kelly heuristic, measured against exact counts | 1.9 | `paper/arxiv_guy_kelly_error_v19/`, `paper/guy_kelly_error.pdf` | [10.5281/zenodo.22063191](https://doi.org/10.5281/zenodo.22063191) |
| The direction spectrum of no-three-in-line solutions: a line model derives its shape, not its scale | 1.1 | `paper/arxiv_direction_spectrum_note_v11/`, `paper/direction_spectrum_note.pdf` | [10.5281/zenodo.22275037](https://doi.org/10.5281/zenodo.22275037) |

The `paper/arxiv_*.zip` files are the arXiv submission packages (sources plus `anc/` ancillary data), each
test-compiled on 10 September 2026.

## OEIS

| entry | contribution | status |
|---|---|---|
| [A399138](https://oeis.org/A399138) — maximum points in the n X n X n grid, no three collinear | new sequence 1, 8, 16, 28, 40, 64, with the witness file `oeis/a399138.txt` | approved Aug 23 2026 |
| [A000755](https://oeis.org/A000755) — plane, number of 2n-point solutions | a(20) = 941580 (from Flammenkamp's database, confirmed by orbit sums) | approved Aug 27 2026 |
| [A280537](https://oeis.org/A280537) — cube, no four coplanar | a(12) >= 31, a(n) <= 3n, configurations for the nonprime sizes 8..18 | approved Sep 08 2026 |
| [A398172](https://oeis.org/draft/A398172) — subsets of the n X n grid with no three collinear points | a(1..7); programs in `oeis/2026-09-10/a398172.txt` | in review |
| [A398184](https://oeis.org/draft/A398184) — maximal such subsets | a(1..7); counts by size in `oeis/2026-09-10/a398184.txt` | in review |
| [A398580](https://oeis.org/draft/A398580) — triangle: the subsets above by size | rows n = 1..7, `oeis/2026-09-10/b398580.txt` | draft, Sep 10 2026 |

## Witnesses and verifiers

`witnesses/` holds the plain-text configurations (one point per line, provenance headers); `verify/` the two
independent verifiers: `verify_witness_lines.py` (no three collinear: exact integer cross products over all
triples) and `verify_witness.py` (no four coplanar: exact 3x3 determinants over all quadruples). Run a verifier
on a file and it says how many bad triples or quadruples it found; the expected answer is zero.

## Licence

Text and data: CC BY 4.0. Code: MIT. See `LICENSE.md`.
