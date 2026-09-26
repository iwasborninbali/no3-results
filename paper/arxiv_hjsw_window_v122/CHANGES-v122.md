# Changes for v1.22

Version 1.22 is a separate copy of v1.21. The v1.21 directory and zip are unchanged. The repository-root README was unchanged by this edit; its v1.22 status row was added afterwards, at integration (commit ad86bc9). No commit, push, network access, package installation or new solver search was performed. The submission zip contains the ten root-level TeX files and `anc/`, without the PDF, build files or this changelog.

## Proof sources and review scope

Inputs are identified by their supplied basenames: `H1-attempt-report.md`, `H2-reviewer-read.md` (a returning reviewer), `H3-clean-read-ru.md` (a clean-context read), and `H4-scripted-read.md` (a scripted read). H2's opening insertion table governs the scopes below. The four arguments in H1 were checked step by step against v1.21's definitions and proved lemmas before insertion. The reads themselves are not redistributed in the submission archive.

No mathematical gap was found in these four arguments within their stated domains. The defective general certificate validator was repaired; it does not invalidate the supplied integer certificates. No finite computation is substituted for an asymptotic proof.

## Claim map

| Statement (label) | v1.21 status | v1.22 status | Source of the proof (input and section) | Check performed |
|---|---|---|---|---|
| PC (`hyp:pair`) | Named hypothesis | Theorem, with uniform pair count for the stated permutation-cubic domain | H1 §PC; H2 §2; H3 PC read | Matched all three five-coefficient configurations to `eq:gamma2`; checked ten disjoint simple branch sets and square-class independence, unused Kummer characters, independent sign changes, bounded poles and uniform character sums. Retained shared membership/root variables, five factors of U, pattern mass 2^-10, shared cubic coordinates and factor 1/(3Q). Checked uniform mesh boundaries and unordered multiplicity one. |
| BT (`hyp:tail`) | Hypothesis for nondegenerate k>9 | Theorem for every nondegenerate k>=2, restricted optimum in the HJSW window | H1 §BT; H2 §3; H3 BT read | `lem:edges` gives four H(1) classes per edge, one generic orbit; a^2=±1 is exactly degeneracy. `lem:orbopt` gives 12 lawful points and `lem:orbdec` permits their union. Checked beta>=12(k-1), 32(k-1) candidates, nonnegativity by rows, and exact 5/256 tail. |
| CP (`hyp:positions`) | Named hypothesis | Theorem under geometric S_k monodromy, branch disjointness and sufficiently large p | H1 §CP; H2 §3; H3 CP read | Exact-size sieve and both factorial normalizations checked; unrestricted tuple irreducibility and transpositions exclude extra linear phases. Projection of full-sum Haar measure onto a proper subtuple is product Haar. Distinguished-root S_(k-1) covers are regular and geometrically disjoint by the tame branch argument. Retained full sums b/p-k*x0/p, complete partner sums, exact threshold tie and uniform endpoint errors. Conditional laws mean disintegration of the joint limiting law. |
| Weaker UM (`thm:weakmargin`) | Absent | New theorem on the whole parameter torus, margin at least 625/108864>1/200 | H1 §UM; H2 §2; H3 weak-UM read; H4 exact checks | Checked lift-table bounds 1/4<=U<=1/2; half-open role uniqueness; at most six neighbours; ordered-to-unordered factor 1/2; deterministic model weights, without arithmetic independence. Base-coordinate sums and fixed meshes give uniform limits; continuity extends to all torus parameters. Exactly integrated floor counts for q=3,63 and independently for q=1..200. |
| Unconditional cubic bound (`thm:cubic2745`) | Absent; 11/4 bound proved | New theorem: alpha(ax^3,B)<=(549/200+o(1))p | H1 §UM consequence; H2 §2 insertion restriction | Uses PC, weak margin, `lem:match`, `lem:cert`; CP and BT are not dependencies. Domain explicitly p≡2 mod 3, a≠0, half-open 2p by 2p integer boxes, error uniform in a and both origins. Checked 549/200=2.745 and stronger raw coefficient 298751/108864. |
| Original UM (`hyp:margin`, `eq:margin`) | Open margin 0.098 | Still open, unchanged | H1 §UM limitation; H2 §2 | Weak proved margin is below 1/12 and below 0.098. Neither quadrature nor finite samples supply the original margin. |
| BS (`hyp:block`) | Open signature invariance and universal table bounds | Still open; new exact finite evidence only | H1 §BS; H2 §5–6; H3 BS read; H4 validator check | Verified every supplied block with integer/Fraction arithmetic, reconstructed metadata, complete unique coverage through 503, and recounted all aggregate claims. Unresolved cases remain explicit. |

The historical labels `hyp:pair`, `hyp:tail` and `hyp:positions` are retained for stable references, but their environments are now theorems.

## Every changed dependency

| Statement or location | Dependency change and retained conditions |
|---|---|
| `prop:counts` | Pair assertion loses PC as an assumption and cites its ten-conic theorem. The single-line proof stays intact. |
| `thm:strong`, first inequality | The bound 11/4-gamma1+gamma2 is unconditional in its stated permutation-cubic domain, uniformly in a and the half-open box. |
| `thm:strong`, 2.652 endpoint and final strict inequality | PC removed; original UM remains necessary for this endpoint and the coefficient 1.326N. |
| `cor:g3` | PC removed; UM retained. G3 is not made unconditional. |
| Numerical-evidence paragraph and final remark in `section_strong.tex` | The 2.652 claim now requires UM alone; the alternative 2.657 claim still requires a proved margin 0.093. A margin strictly above 1/12 still suffices for G3, using proved PC. Historical finite experiments remain evidence only. |
| Final remark of `lemma_fe.tex` | Replaced the obsolete unproved-PC statement with the separate ten-conic theorem; the six-conic lemma is not substituted for that proof. |
| `cor:blockconst`, tail interval | BT removed as an assumption; proved BT supplies the 5/256 tail, with p tending to infinity at each fixed cutoff before the cutoff tends to infinity. |
| `cor:blockconst`, table coefficient and whole certificate interval | BS remains required for the sampled table and signature invariance. No new uniform estimate for a p-growing run length or unrestricted optimum is asserted. |
| `lem:positions`, exactly-sized fibres | CP removed as an assumption; exact-size inclusion–exclusion supplies the missing step, using only the independently proved unrestricted tuple argument. Full-split relations remain. |
| `lem:twoslopes`, positions | CP removed as an assumption; retained p>k!, excluded resultant primes, disjoint finite branch loci, full partner sums and threshold tie. CP's proof uses only the independent geometric branch argument from this lemma, not its position conclusion. |
| `thm:perm`, k>=5 | CP removed as an assumption; fixed odd degree, permutation condition, resultant exclusions and sufficiently large primes retained (p>k! explicit). Full-split correction and cubic special case retained. |
| `cor:permgen` | CP removed as an assumption; geometric S_k monodromy is explicit, coprime discriminants and sufficiently large p>k! retained. |
| Arbitrary-monodromy paragraph after `cor:permgen` | Analogous position law remains conditional, with its own irreducibility and linear-disjointness requirements. The all-fixed-degree permutation-polynomial question remains open. |
| Abstract, extended summary, introduction, cubic-section final remark, appendix (b)–(c), reproduction notes | Updated precisely to the dependencies above; no global replacement of “conditional”. |

`cor:rundensity` still gives densities unconditionally and uses BS for table-based savings. `thm:blocks`, `lem:match`, `lem:cert`, the orbit lemmas, `thm:cubic` and `cor:cubic` keep their established status. The possible extension of 2.745 to all cubics suggested by the clean-context read was **not inserted**: the new theorem is limited to the explicit monomial permutation-cubic domain accepted by all reads. The older all-cubic exclusion theorem remains unchanged.

## Exact arithmetic and finite certificates

`anc/verify_v122.py` has its own standard-library arithmetic and independent reference construction of the p=11 block from xy=1 and reflection. It checks:

- Floor integrals: I3=10/9 and I63=250/189 are lower bounds on the respective geometric densities, not identities asserting constant densities. Their product is 2500/1701; gamma1>=625/27216; the neighbour factor is 3/4; margin>=625/108864. The difference from 1/200 is 2017/2721600, and 11/4-1/200=549/200. The exact stronger coefficient is 298751/108864.
- CP: 816 sieve cases for 0<=j<=r<=k<=15, 120 size-biased partner identities, normalization, and independent rencontres checks by derangements and permutations through degree seven.
- BT: 999 exact length checks of the arithmetic, the infinite geometric tail 5/256, independent descent enumeration through length nine, table saving 68350729/123863040, coefficient 427101431/123863040 and lower endpoint 424682231/123863040. These table coefficients still require BS mathematically.
- The repaired verifier as a regression subject: honest p=11, run [3,4,5] returns (24,24); the forged witness 0.5,...,63.5 with all-zero duals, upper "64" and interval [64,64] is rejected specifically for noninteger indices. Boolean indices, false signatures, false intervals, duplicate blocks, missing blocks and a false summary count are also rejected.

The verifier requires `type(i) is int` before the witness range check, compares reconstructed signatures and computed intervals with saved metadata, compares the unique block keys with the generator for every odd prime through 503, and recomputes saved and additional summary counts. Explicit exceptions keep validation active even under `python3 -O`. NumPy/SciPy imports are needed only for optional regeneration; exact verification uses the standard library.

The attempt's `block_search.json` remains byte-identical, SHA-256 `b0122df8aeaae2f7d6b2ccd5a0ed7e5558a3241587ba21e820f46bd25cf1d551`. Recomputed results: 95 odd primes; 2707 blocks; lengths 2–11; 105 signatures; 2582 exact optima; 125 unresolved optimum intervals. Of 2702 blocks of length at most nine, 2578 certify the table lower saving and 124 remain unresolved. There are zero certified table violations or conflicting exact savings for one signature; this does not exclude violations in unresolved cases. The README claim is “exact finite certificates for p <= 503; BS remains open”.

`verify_v121.py` and `verify_v120.py` are retained unchanged. New jobs are `bs_certificates` and `v122_formulas`. Historical numerical diagnostics still do not certify original UM or BS. The finite BS solver search and the attempt's extra UM grid/Sobol searches were not rerun.

## Version, provenance and portability

The title-page version is 1.22, with the requested version-history entry. The existing AI disclosure is retained and extended by the requested sentence crediting OpenAI Codex (GPT-6) and three independent reads (two OpenAI GPT-6 agents and one Claude Opus 5.5 agent with exact scripted checks).

Local path spellings in 16 inherited archival text files were normalized to portable paths, without changing numerical evidence. `anc/SOURCE.json` records each before/after hash and the provenance of the new files; historical source hashes are not overwritten. The fresh run log with an absolute ancillary-directory prefix is also normalized to `anc/`. No absolute local paths are shipped. No prohibited names from the supplied reads are copied into the archive.

## Build, execution and archive

- `python3 run_all.py` from `anc/` completed with **45 jobs: 43 PASS, 2 NOT RUN, 0 FAILED** (CPython 3.14.6, NumPy 2.5.2, SciPy 1.18.0). `block_cover` and `sat_dependency` remain NOT RUN because PySAT is unavailable; the optional PySAT stage of `boxes` also reports its skip. All nonoptional checks passed. Exact commands, exit codes, times and key output are in `anc/RUNS.md` and `anc/runs/results.json`.
- Direct `python3 -B verify_v122.py`: **ALL v1.22 checks passed**, exit 0. The batch job also passed. Direct `python3 -B bs_search/search_blocks.py --verify`: **EXACT VERIFICATION PASSED 2707**, exit 0; the batch job also passed.
- In the v1.22 package directory, `pdflatex -interaction=nonstopmode -halt-on-error hjsw_window.tex` completed **three times**, each with exit 0. The final log has no errors, warnings, undefined references or undefined citations. PDF: **51 pages**, 837771 bytes. The first two passes resolved cross-references; only the final pass is used for the clean-reference assertion.
- `anc/MANIFEST.sha256` was regenerated and every one of its **347** entries verified after the runs and documentation updates. The manifest covers all ancillary files except itself.
- `paper/arxiv_hjsw_window_v122.zip`: **358 files**, ten TeX files at the root plus `anc/`, with no PDF, auxiliary/build files or CHANGES file. No directory entries or enclosing package directory. ZIP CRCs and every archived file's bytes match the final package.
- Zip SHA-256: `22be186bc480610e592f79a19e41336fc335f24ffb706ea2903ef70105cc3e5a`.
- Case-insensitive forbidden-name occurrences in all decompressed zip member contents: **0**; member names also pass. Absolute local path scan: **0**.
- A final SHA-256 comparison against the initial snapshot confirms **all 359 checked files** in v1.21 (including its zip) and the repository-root README remain byte-identical. Only the new v1.22 directory and zip are new workspace artifacts. No commit or push.
