# Exact n = 10 no-three-in-line count profile (5 November 2026)

**Status:** complete exhaustive count; two independently written programs agree in every cell of the ordinary, maximal and addable-point profiles. The row-pattern program and integer-determinant program each completed 512 of 512 shards. Labelled subsets (not symmetry classes) are counted.

| Quantity | Exact value |
|---|---:|
| All safe subsets, including the empty set | 7,287,023,194,031 |
| Inclusion-maximal safe subsets | 56,412,888,628 |
| Peak of the ordinary size profile | 12 points |
| First layer with more maximal than extendable sets | 17 points |
| 20-point sets (previously known endpoint; not a new result) | 1,135 |

- [`profile-n10.json`](profile-n10.json): all 21 cells of the three profiles and aggregate hashes.
- [`shards-n10.tar.gz`](shards-n10.tar.gz): the 1,024 JSON shard outputs, 1,024 per-output SHA-256 receipts, plan, aggregate and build manifest. **SHA-256:** `ae416edb0856c8c08c01b781cd2919ab2664ef516b5eb07644b925b3243d6044` (438,032 bytes). Only this computation's verified JSON data are included, no executables, SSH material or logs. The archive's provenance includes VM PIDs and timings; the counters and outputs are independent of those values.
- Original VM `run-n10/aggregate.json` SHA-256: `1e41481ff0784725d8ec61d29e571683bf62c2e0e3911142d23eff3845926b1f`, reproduced after reaggregation on a separate local machine. Public sources [`line_rows.c`](../../line_rows.c), [`determinant_check.c`](../../determinant_check.c) and [`collect.py`](../../collect.py) have the same SHA-256 values as the VM build manifest in the archive.

## Recheck (standard Python; no long enumeration needed)

Extract `shards-n10.tar.gz` into a **new empty directory**, inspect archive members before extracting, and use Python 3.12+ with the data-only extraction filter. From this directory, for example:

```sh
mkdir n10-check
python3 -I - <<'PY'
import pathlib, tarfile
root=pathlib.Path('n10-check')
with tarfile.open('shards-n10.tar.gz') as archive:
    members=archive.getmembers()
    assert all(m.isfile() and not m.name.startswith('/') and '..' not in pathlib.PurePosixPath(m.name).parts for m in members)
    archive.extractall(root, filter='data')
PY
python3 -I ../../collect.py n10-check/run-n10 --require-complete
python3 -I -c "import hashlib; print(hashlib.sha256(open('n10-check/run-n10/aggregate.json','rb').read()).hexdigest())"
```

The collector checks every receipt's output hash, build/plan identity, frontier partition and per-shard profiles; at completion it checks small-size combinatorics, addable-point ledger, maximal counts and the known endpoint, then compares the two programs cell by cell. This is a repeatable audit of stored outputs; **independent re-enumeration** means running the public C programs on all shards, not merely rerunning the collector. A receipt alone does not prove that the encoding matches the mathematical definition; the two programs implement different tests, and small-n profiles serve as controls.

## Before-data forecast score

Two heuristic forecasts, Q (density-scaled quota correction) and H (fixed-hole correction), were frozen before the **completed** n = 10 count in a separate private lab repository. Their **byte-identical** [Markdown](predictions-n10.md) and [numeric JSON](predictions-n10.json) are included here for public inspection; their hashes were [publicly witnessed on rStation](https://rstation.ai/r/no_three_in_line/posts/92): SHA-256 `71a4749ee137b1d1c97879964baefab2e6fde76f2b8ddc53c5f311efc07f315c` and `cdf9f54d9c01156975fb0282703d7c7ad434484aea4e1733cc5e81aa7152ddf3`. Neither frozen file was changed to fit the final count. **Blindness limitation:** shard receipts indicate that 19 row-pattern and 15 determinant shards had already finished before the forecast's stated creation time, and 192 row-pattern and 193 determinant shards before the public hash witness. The forecaster declared that they had not inspected the n = 10 enumeration files; the public witness establishes file identity at that later time, **not** that no partial results existed or that this non-inspection claim is independently proven. An estimate of the n = 10 total was also disclosed to the forecaster and is documented in the frozen files. Interpret this as a conditionally blind, finite forecast, not an experiment with zero exposure.

Under the **predeclared** primary WIS score (lower is better), Q scored **0.211679**, H **0.239179**. Their 0.027500 difference clears the stated 0.01 finite-forecast decision gate: Q wins this *one n = 10 comparison*, subject to the exposure limitation above. Both predicted the peak at 12 and the first majority-maximal layer at 17; each has absolute error 0, IS80 2, and interval coverage for both secondary targets. Both covered 8/8 logarithmic count targets and 6/6 logarithmic maximal-count targets with nominal 80% intervals; this one board does **not** establish interval calibration. H had the smaller MAE on maximal counts despite the larger total WIS. A predicted split of endpoint-completable components is unscored until a separate graph census. Neither finite forecast decides whether the asymptotic Guy–Kelly remainder grows like n or n log n.

Run `python3 -I score_forecast.py profile-n10.json predictions-n10.json` from this directory to reproduce the score without changing the frozen forecast.

Code MIT; data and this text CC BY 4.0. Initial enumeration and controls: Athanor lab; the 1,135 endpoint was established previously and is not claimed as ours. No n = 11 exhaustive run or OEIS update is implied by this release.
