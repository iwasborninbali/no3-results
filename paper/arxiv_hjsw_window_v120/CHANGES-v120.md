# Changes for v1.20

Prepared in the hjsw-v120 worktree. No commit, push, network access, or writes to the source repositories. The ten v1.19 TeX files are unchanged.

The unconditional single-hyperbola results, conic projection result, eight-point and clean-seven covers and asymptotics, block decomposition, potential cover, large-order consequence, and cubic 11p/4 bound are retained. No numbered result has been deleted or renumbered. Theorem 54 retains the proved cubic case and exact model arithmetic, but its k>=5 arithmetic consequence is conditional: R1 identified a conditioning gap despite R2 listing the theorem among its surviving results. This resolves the two reads conservatively under the instructed honest-status route.

## Named hypotheses

- **BS**: arithmetic block saving is signature-dependent and bounded below by the minimum recorded model saving through length nine.
- **BT**: every longer nondegenerate block has saving at most 4(k-1); used only for the tail interval.
- **CP**: root positions conditional on exact fibre size, with full-split relations and joint two-slope law.
- **PC**: uniform intersecting-pair count for the explicitly defined shared-variable model integral.
- **UM**: gamma1 - gamma2 >= 0.098 over the entire two-dimensional box torus.

None of these five hypotheses is asserted proved. Exact integral/table arithmetic is distinct from applicability to arithmetic configurations.

## Numbered claim map

Numbers are the actual LaTeX theorem-counter numbers, including gaps occupied by remarks. Every theorem, corollary, proposition and lemma is listed. No numbered empirical result is introduced; finite observations occur in remarks and Section 11.

| Claim | Label | Status | v1.20 source |
|---|---|---|---|
| Theorem 1 | `thm:main` | Proved. | [hjsw_window.tex:117](hjsw_window.tex#L117) |
| Corollary 2 | `cor:qr` | Proved. | [hjsw_window.tex:130](hjsw_window.tex#L130) |
| Theorem 3 | `thm:window` | Proved. | [hjsw_window.tex:136](hjsw_window.tex#L136) |
| Lemma 4 | `lem:lagrange` | Proved. | [hjsw_window.tex:219](hjsw_window.tex#L219) |
| Lemma 5 | `lem:copies` | Proved. | [hjsw_window.tex:238](hjsw_window.tex#L238) |
| Corollary 6 | `cor:slopes` | Proved. | [hjsw_window.tex:250](hjsw_window.tex#L250) |
| Lemma 7 | `lem:partners` | Proved. | [hjsw_window.tex:261](hjsw_window.tex#L261) |
| Proposition 8 | `prop:lines` | Proved. | [hjsw_window.tex:299](hjsw_window.tex#L299) |
| Lemma 10 | `lem:orbit` | Proved. | [hjsw_window.tex:498](hjsw_window.tex#L498) |
| Lemma 11 | `lem:gadget` | Proved. | [hjsw_window.tex:553](hjsw_window.tex#L553) |
| Corollary 12 | `cor:conics` | Proved. | [hjsw_window.tex:626](hjsw_window.tex#L626) |
| Corollary 15 | `cor:no4` | Proved. | [hjsw_window.tex:664](hjsw_window.tex#L664) |
| Lemma 17 | `lem:orbdec` | Proved. | [lemma_stability.tex:7](lemma_stability.tex#L7) |
| Lemma 18 | `lem:orbopt` | Proved. | [lemma_stability.tex:24](lemma_stability.tex#L24) |
| Proposition 19 | `prop:stability` | Proved. | [lemma_stability.tex:40](lemma_stability.tex#L40) |
| Theorem 21 | `thm:two` | Proved. | [hjsw_window.tex:745](hjsw_window.tex#L745) |
| Lemma 22 | `lem:rowsRR` | Proved. | [hjsw_window.tex:754](hjsw_window.tex#L754) |
| Lemma 23 | `lem:groups` | Proved. | [hjsw_window.tex:764](hjsw_window.tex#L764) |
| Lemma 24 | `lem:closure` | Proved. | [hjsw_window.tex:787](hjsw_window.tex#L787) |
| Proposition 25 | `prop:m8` | Proved. | [hjsw_window.tex:817](hjsw_window.tex#L817) |
| Proposition 26 | `prop:m8asym` | Proved. | [hjsw_window.tex:839](hjsw_window.tex#L839) |
| Lemma 28 | `lem:klein` | Proved. | [section_seven.tex:18](section_seven.tex#L18) |
| Lemma 29 | `lem:neighbours` | Proved. | [section_seven.tex:40](section_seven.tex#L40) |
| Theorem 30 | `thm:seven` | Proved. | [section_seven.tex:61](section_seven.tex#L61) |
| Proposition 31 | `prop:m7asym` | Proved. | [section_seven.tex:75](section_seven.tex#L75) |
| Proposition 32 | `prop:clean` | Proved. | [section_seven.tex:90](section_seven.tex#L90) |
| Lemma 34 | `lem:edges` | Proved. | [section_blocks.tex:16](section_blocks.tex#L16) |
| Theorem 35 | `thm:blocks` | Proved. | [section_blocks.tex:40](section_blocks.tex#L40) |
| Lemma 36 | `lem:run` | Proved. | [lemma_run.tex:4](lemma_run.tex#L4) |
| Proposition 37 | `prop:descent` | Proved. | [lemma_run.tex:32](lemma_run.tex#L32) |
| Corollary 38 | `cor:rundensity` | Proved (fixed-length density and implication from certified lower savings); using the sampled table requires BS. | [lemma_run.tex:58](lemma_run.tex#L58) |
| Corollary 39 | `cor:blockconst` | Conditional on BS for the finite-cutoff bound and coefficient; BS + BT for the tail interval. Exact weighted-table arithmetic is checked independently. | [section_blocks.tex:77](section_blocks.tex#L77) |
| Theorem 41 | `thm:general` | Proved. | [hjsw_window.tex:967](hjsw_window.tex#L967) |
| Proposition 42 | `prop:g8k` | Proved. | [hjsw_window.tex:1004](hjsw_window.tex#L1004) |
| Lemma 43 | `lem:arc` | Proved. | [hjsw_window.tex:1016](hjsw_window.tex#L1016) |
| Corollary 44 | `cor:general` | Proved. | [hjsw_window.tex:1065](hjsw_window.tex#L1065) |
| Lemma 46 | `lem:projection` | Proved. | [section_cubic.tex:33](section_cubic.tex#L33) |
| Theorem 47 | `thm:cubic` | Proved. | [section_cubic.tex:71](section_cubic.tex#L71) |
| Corollary 48 | `cor:cubic` | Proved. | [section_cubic.tex:230](section_cubic.tex#L230) |
| Lemma 50 | `lem:lifts` | Proved. | [section_perm.tex:23](section_perm.tex#L23) |
| Lemma 51 | `lem:rootcounts` | Proved. | [section_perm.tex:58](section_perm.tex#L58) |
| Lemma 52 | `lem:positions` | Proved for unrestricted ordered root tuples; consequences conditional on CP for fibres with exactly j roots. | [section_perm.tex:81](section_perm.tex#L81) |
| Lemma 53 | `lem:twoslopes` | Proved for root-count independence and disjointness; conditional on CP for root positions. | [section_perm.tex:106](section_perm.tex#L106) |
| Theorem 54 | `thm:perm` | Proved for k=3 independently via Theorem 47; conditional on CP for fixed odd k>=5. Model integrals and correction accounting retained. | [section_perm.tex:152](section_perm.tex#L152) |
| Corollary 55 | `cor:permgen` | Conditional on CP for the stated fixed-degree family, in addition to its monodromy and discriminant hypotheses. | [section_perm.tex:175](section_perm.tex#L175) |
| Lemma 57 | `lem:cert` | Proved. | [section_strong.tex:25](section_strong.tex#L25) |
| Lemma 58 | `lem:match` | Proved. | [section_strong.tex:34](section_strong.tex#L34) |
| Lemma 59 | `lem:fe` | Proved. | [lemma_fe.tex:4](lemma_fe.tex#L4) |
| Proposition 61 | `prop:counts` | Proved for the single-line count using corrected Lemma FE; conditional on PC for the pair count. | [section_strong.tex:141](section_strong.tex#L141) |
| Theorem 62 | `thm:strong` | Conditional on PC + UM. | [section_strong.tex:186](section_strong.tex#L186) |
| Corollary 63 | `cor:g3` | Conditional on PC + UM. | [section_strong.tex:200](section_strong.tex#L200) |

## Finding-by-finding resolutions

| Finding | Resolution | Change and limits | v1.20 locator |
|---|---|---|---|
| R1 B1 | Downgraded / fixed | Strong theorem and G3 now assume PC and UM. Full two-parameter integral domains, finite shared-role list, unordered multiplicities and shared conic variables are explicit. Withdrawn interpolation allowance; 2.652 uses 0.098, 2.657 would use 0.093; discrepancy ratio corrected. Table hybrid estimates are separated from continuum quadrature. | [section_strong.tex:55](section_strong.tex#L55); [section_strong.tex:153](section_strong.tex#L153); [section_strong.tex:186](section_strong.tex#L186) |
| R1 B2 | Fixed / downgraded | Corrected direction and additive phase, irreducible-curve main term p, and 2^-6 pattern mass. Root-swap invariance imposed and every strong-section root event checked. Pair extension isolated as PC. | [lemma_fe.tex:4](lemma_fe.tex#L4); [lemma_fe.tex:49](lemma_fe.tex#L49); [section_strong.tex:134](section_strong.tex#L134) |
| R1 B3 | Downgraded / fixed | BS names configuration invariance and recorded minima as universal lower bounds; BT separately names the tail bound. All eight ambiguous rows and loss of configuration/point-count/solver information disclosed. Exact tail 5/256. No new universal block certificates claimed. | [section_blocks.tex:67](section_blocks.tex#L67); [section_blocks.tex:104](section_blocks.tex#L104); [lemma_run.tex:64](lemma_run.tex#L64) |
| R1 M1 | Downgraded / fixed | Unrestricted tuple result retained; missing exactly-j conditioning is CP. Dependent monomial/generic-family statements cite CP. Ramification is containment with large-characteristic tameness. NR82 restricted to Theorem 9 and Corollary 2 on binomials; general complete-mapping exclusion withdrawn. | [section_perm.tex:4](section_perm.tex#L4); [section_perm.tex:106](section_perm.tex#L106); [section_perm.tex:203](section_perm.tex#L203) |
| R1 M2, bullet 1 (component laws / finite-table obstruction) | Removed / downgraded | Removed universal O(log p), p^(2/3), only-k=-1 and uselessness conclusions. Retained finite component data at p=4001, explicitly empirical. | [section_blocks.tex:144](section_blocks.tex#L144) |
| R1 M2, bullet 2 (mirrored-orbit optima) | Downgraded | Mirrored-pair maxima are finite observations for primes <=23. Removed all-prime classification and implied certificate obstruction. | [section_blocks.tex:149](section_blocks.tex#L149) |
| R1 M2, bullet 3 (regression exclusion) | Removed / downgraded | Regressions describe only the exact small-prime range ending at p=19; p=23 remains unresolved. Conditional linear-gap explanation gives both unproved premises. | [hjsw_window.tex:1121](hjsw_window.tex#L1121); [hjsw_window.tex:1127](hjsw_window.tex#L1127) |
| R1 M2, bullet 4 (vertical-pair claims) | Downgraded | All three proposed facts and the trace/edge estimates are unproved programme claims. Gaussian-norm sketch withdrawn as a proof; Rayleigh implication clearly conditional. | [hjsw_window.tex:1141](hjsw_window.tex#L1141) |
| R1 section 4, item 1 | Fixed | u4=-u1+u2-u3 now agrees with the volume calculation. | [section_seven.tex:127](section_seven.tex#L127) |
| R1 section 4, item 2 | Fixed | All stability summaries use one-sided \|S\M\|<=t and symmetric difference <=3t; the single-orbit proof is now a direct incidence count. | [lemma_stability.tex:5](lemma_stability.tex#L5); [hjsw_window.tex:54](hjsw_window.tex#L54) |
| R1 section 4, item 3 | Fixed | Two lifted rows contain 4\|f^-1(c)\| candidates; lawful row bound unchanged. | [section_cubic.tex:37](section_cubic.tex#L37) |
| R1 section 4, item 4 | Fixed | W4 uses >=4 while rich means >=3. Older G3 remark agrees with conditional PC/UM status. | [section_cubic.tex:84](section_cubic.tex#L84); [section_cubic.tex:252](section_cubic.tex#L252) |
| R1 section 4, item 5 | Fixed / downgraded | Model Ck, finite-p costs and bound including epsilon separated. Degree-five 2.945933 (about 1.473N); true-asymptotic numerical claim withdrawn. | [section_perm.tex:6](section_perm.tex#L6); [section_perm.tex:195](section_perm.tex#L195) |
| R1 section 4, item 6 | Fixed | Inverse map comparison restricts to occupied nontangent residues, separates exceptions, HJSW window and O(1); arbitrary boxes use Theorem 3. | [section_perm.tex:199](section_perm.tex#L199) |
| R1 section 4, item 7 | Fixed | Union appendix keeps o(1) in conversion to n; clean-seven strict margin is separate. Finite checks do not certify asymptotics. | [appendix_hyperbolae.tex:13](appendix_hyperbolae.tex#L13); [appendix_hyperbolae.tex:33](appendix_hyperbolae.tex#L33) |
| R1 section 4, item 8 | Fixed | Elementary/self-contained applies to single-hyperbola incidence core; later estimates explicitly use cited character sums/Chebotarev. | [hjsw_window.tex:56](hjsw_window.tex#L56) |
| R1 section 5 (attribution / novelty) | Fixed | Published KNS citation updated to Advances in Combinatorics 2026:7, 18 September 2026, arXiv v2. Qualitative S2/S3 optimality credited; note positioned as proof/classification/enumeration/arbitrary-window formulas and qualified extensions. No new priority search claimed. | [hjsw_window.tex:48](hjsw_window.tex#L48); [hjsw_window.tex:1228](hjsw_window.tex#L1228) |
| R1 section 5 (Green) | Fixed | Problem 72 motivates restricted-family questions, not a settled problem or exhaustive classification. | [hjsw_window.tex:42](hjsw_window.tex#L42); [appendix_hyperbolae.tex:34](appendix_hyperbolae.tex#L34) |
| R1 section 5 (availability / tag / certificates) | Fixed | anc is evidence of record at the specified saturation commit; source hashes, adaptations, exact commands, fresh runs and historical reports are distinguished. No nonexistent immutable tag or new exact MILP certificate. | [hjsw_window.tex:1165](hjsw_window.tex#L1165); [hjsw_window.tex:1185](hjsw_window.tex#L1185) |
| R2 item 1 | Downgraded / fixed | PC + UM throughout; uniform-margin gap not closed by numerical samples. Corrected discrepancy comparison and coefficient mismatch. | [section_strong.tex:153](section_strong.tex#L153); [hjsw_window.tex:40](hjsw_window.tex#L40) |
| R2 item 2 | Fixed / downgraded | Corrected ac1*u^3, additive phase, p+O(sqrt p), fair membership mass and symmetric-root scope; pair law conditional. | [lemma_fe.tex:4](lemma_fe.tex#L4); [lemma_fe.tex:49](lemma_fe.tex#L49) |
| R2 item 3 | Downgraded | 510-row table retained as a sampled model. No incidence-invariance theorem or exact universal certificate invented; BS and BT name the missing bridges. | [section_blocks.tex:67](section_blocks.tex#L67); [section_blocks.tex:104](section_blocks.tex#L104) |
| R2 item 4 | Fixed / downgraded | All summaries qualify nondegenerate conics p>=11, asymptotic cubics and fixed-degree monomials, including epsilon and CP. Finite p=5 cubic exception explicitly checked; x^(p-2) excluded from fixed-degree scope. | [hjsw_window.tex:31](hjsw_window.tex#L31); [section_cubic.tex:236](section_cubic.tex#L236); [section_perm.tex:8](section_perm.tex#L8); [appendix_hyperbolae.tex:18](appendix_hyperbolae.tex#L18) |
| R2 item 5 | Removed / downgraded | Random-graph conclusions withdrawn; finite component observations retained with their range. | [section_blocks.tex:144](section_blocks.tex#L144) |
| R2 item 6 | Removed / downgraded | No finite regression excludes asymptotics, no universal certificate lower barrier, no asserted true saving. Restricted LP, restricted integer and unrestricted maxima separated. | [hjsw_window.tex:1121](hjsw_window.tex#L1121); [hjsw_window.tex:1127](hjsw_window.tex#L1127) |
| R2 item 7 | Downgraded | Vertical-pair form/classification/lower bound and trace estimate are unfinished programme claims, not proved facts. | [hjsw_window.tex:1141](hjsw_window.tex#L1141) |
| R2 item 8 | Fixed | Dependencies, tables, archived logs and drivers included in anc. All executable entry points have documented jobs; PySAT exceptions are explicit, optional MIP stage is skipped. SymPy source is archived with a documented exact Fraction port. | [hjsw_window.tex:1165](hjsw_window.tex#L1165) |
| R2 item 9 | Fixed | KNS qualitative optimality credited and publication updated; Green motivation narrowed. | [hjsw_window.tex:48](hjsw_window.tex#L48); [hjsw_window.tex:42](hjsw_window.tex#L42); [hjsw_window.tex:1228](hjsw_window.tex#L1228) |
| R2 item 10 | Fixed | Group densities 1/12 each sum to 1/4; seven-sign correction; sufficiently large p in run lemma; one-sided and symmetric stability distances distinguished. | [hjsw_window.tex:1137](hjsw_window.tex#L1137); [section_seven.tex:127](section_seven.tex#L127); [lemma_run.tex:5](lemma_run.tex#L5); [lemma_stability.tex:5](lemma_stability.tex#L5) |
| R3 a | Fixed | Corrected irreducible-curve point count and membership normalization; exact conic counts checked at 101,1009,1013. | [lemma_fe.tex:49](lemma_fe.tex#L49) |
| R3 b | Fixed | Corrected family direction and additive phase, consistent with 63az^3 for (1,3). | [lemma_fe.tex:7](lemma_fe.tex#L7); [section_strong.tex:18](section_strong.tex#L18) |
| R3 c | Fixed / downgraded | All eight multivalued signatures retained and listed; recorded minima are not universal bounds without BS. | [section_blocks.tex:104](section_blocks.tex#L104) |
| R3 d | Fixed / downgraded | 2.652 and 2.657 reconciled as two different assumed margins; no invented allowance. | [section_strong.tex:167](section_strong.tex#L167) |
| R3 e | Fixed | Nonexistent tag replaced by anc plus the specified immutable source commit. | [hjsw_window.tex:1185](hjsw_window.tex#L1185) |
| R3 f | Fixed | Nine core scripts and all imports are bundled. Explicit p,k/pair/list arguments resolve silent scripts; numpy/scipy requirements and PySAT skips are recorded. | [hjsw_window.tex:1174](hjsw_window.tex#L1174) |

## Evidence and build

`anc/README.md` gives exact commands and expected outputs; `anc/RUNS.md` records actual executions, status, timing and key lines. `anc/SOURCE.json` records every upstream source/data hash and portability or arithmetic adaptations. The original SymPy integrator is archived as text; its portable executable uses the independently checked Fraction implementation. Model output regeneration is redirected to `anc/runs/generated/`, preserving committed tables and logs.

PySAT-dependent entry points and the optional box MIP stage cannot run here because PySAT is absent. No SAT or MILP report is relabelled an independently checked exact certificate. The model invariance, uniform margin and conditioning/pair-count bridges are deliberately unresolved mathematical hypotheses, not unfinished editorial corrections.

Final validation (26 September 2026):

- Ran `pdflatex -interaction=nonstopmode -halt-on-error hjsw_window.tex` twice from this directory after the final TeX edits; both exited 0. The bibliography is inline, so BibTeX was not needed. The final log has no errors, warnings, undefined references, or overfull/underfull boxes. The retained PDF has 46 pages; its first page and the repaired FE page were visually inspected.
- `anc/RUNS.md`: **40 passing jobs, 2 NOT RUN, zero failed jobs**. The two NOT RUN entries require absent PySAT; the completed box checker also skipped its optional PySAT-dependent MIP stage. Every one of the 41 active Python files is covered by a documented job or is an exercised driver. Fresh runs use `/opt/homebrew/bin/python3.14`; their exact finite scopes and quadrature grids are recorded, with no claim of a universal numerical certificate.
- All 267 retained upstream source/data files match their original hashes, except the six documented adaptations, whose originals are retained and hash-checked. Unrelated correspondence and exploratory files were removed from the initial ancillary selection. All scripts cited by the TeX and all local imports are included. Every v1.19 file is byte-identical to `HEAD`.
- `anc/MANIFEST.sha256` covers all 342 other ancillary files. Every digest was checked against the archive contents. The manifest itself is necessarily excluded from its own digest list.
- `../arxiv_hjsw_window_v120.zip` contains exactly the ten TeX files and `anc/` (353 files), with no PDF, LaTeX auxiliary files, or this report. ZIP CRC checks and byte-for-byte comparison with the source package passed.
- ZIP SHA-256: `3c20670fd838661ece1301dbdf6e3cde2f875eb7619f4219cd6a43518500f132`.
- PDF SHA-256: `c5a5bfa31443af48e6929e01c6f00eaa235b26fe2ee66f28da6af8693fc57ac1`.

The requested editorial resolutions are complete. BS, BT, CP, PC, and UM remain mathematical hypotheses; no uniform quadrature enclosure, universal block certificate, or missing conditioning/pair-count proof was manufactured. The finite vertical-pair and regression programmes remain explicitly unproved. No commit or push was made.

## Packaging pass

- Removed the three internal audit letters from the public bundle and their manifest entries; the letters are filed outside the package. Replaced internal naming with neutral audit descriptions and the requested AI-disclosure sentence. No theorem, proof, constant, or mathematical status changed; the other nine TeX files are byte-identical to the pre-pass package.
- Made interpreter commands portable ("python3 (3.14, with numpy)") and source paths relative. Re-ran the independent constants and v1.20 formula jobs; documented prefix-only normalization of historical evidence in `anc/RUNS.md`. All 267 upstream source/data hashes, including six archived originals, still match.
- Regenerated `anc/MANIFEST.sha256` (339 entries). Direct `verify_v120.py` result: `ALL v1.20 checks passed`; the recorded batch remains 40 PASS, 2 NOT RUN, zero failures. PDF rebuilt with two successful pdflatex passes: 46 pages, no errors or undefined references.
- Rebuilt the ZIP with exactly ten TeX files and `anc/` (350 files); no PDF, build auxiliaries, or this report. ZIP CRC, source-byte comparison, manifest digests, unchanged numerical results, and packaging scans passed. Remaining prohibited-word matches: 0; absolute local-path matches outside verbatim upstream files: 0.
- ZIP SHA-256: `1dcc78e6f64eadcb433038ff70447c1c5b078089ca19b4b9c2612eb9d3a4cf45`. No network, commit, or push.
