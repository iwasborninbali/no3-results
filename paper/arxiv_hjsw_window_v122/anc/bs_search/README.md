# Finite BS certificates

**exact finite certificates for p <= 503; BS remains open**

The search covers every maximal nondegenerate run with at least one edge at all 95 odd primes through 503, in the fixed HJSW window. The optimum is restricted to rows, columns and the two diagonal slopes. It is not the unrestricted no-three-in-line optimum and does not range over translated windows.

The supplied `block_search.json` is the attempt's original certificate data, unchanged (SHA-256 `b0122df8aeaae2f7d6b2ccd5a0ed7e5558a3241587ba21e820f46bd25cf1d551`). Floating LP/MILP solvers proposed the witnesses and dual multipliers. Verification uses only integer and rational arithmetic; a solver's status or approximate objective is not a certificate.

For a selected subset, each restricted line must contain at most two selected points. Nonnegative rational line weights y give the upper bound

```text
floor(2*sum(y) + sum_over_points(max(0, 1 - incident_weight)))
```

The point deficits use the constraints that a point can be selected at most once. Equal lower and upper endpoints certify an exact optimum; unequal endpoints remain unresolved.

From `anc/`:

```sh
python3 bs_search/search_blocks.py --verify
python3 verify_v122.py
```

The verifier requires `type(i) is int` for every witness index before checking its range, uniqueness and incidence constraints. It reconstructs and compares the signature and beta interval, checks the complete unique block list against the generator for every odd prime through 503 (including primes with no eligible block), and recomputes all saved summary fields and table comparisons. It uses explicit exceptions, so these checks remain active with Python optimization enabled.

The negative regression replaces the p=11, run [3,4,5] witness by 0.5,...,63.5, sets all duals to zero, and supplies upper bound "64" and interval [64,64]. It must be rejected for noninteger indices; the honest row must return (24,24). The independent v1.22 driver also reconstructs that block directly from xy=1 and reflection and rejects Boolean indices, altered signatures and intervals, missing or duplicate blocks, and a false summary count.

| Recomputed quantity | Value |
|---|---:|
| Blocks | 2707 |
| Length range | 2–11 |
| Distinct signatures | 105 |
| Exact optima | 2582 |
| Unresolved optimum intervals | 125 |
| Blocks of length at most nine | 2702 |
| Certified table lower bounds on saving | 2578 |
| Unresolved table bounds | 124 |
| Certified table violations / conflicting exact savings | 0 / 0 |

These results do not exclude a violation in the unresolved cases. They do not prove signature invariance or the universal table bounds of BS.

Optional regeneration, requiring NumPy and SciPy, is `python3 bs_search/search_blocks.py 503` from `anc/`; it replaces the local certificate file. This generation was not rerun for v1.22: the supplied certificates were reverified exactly. Solver candidate choices can differ between environments. The registered `bs_certificates` job only verifies the supplied data and needs the standard library.
