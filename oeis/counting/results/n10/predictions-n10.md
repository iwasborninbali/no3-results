# n=10 predictions — preregistration v1.0

Frozen 2026-11-03T20:16:42.707826+00:00 (UTC); 2026-11-04T04:16:42.707826+08:00 (WITA).

All predictions are **heuristic**. Natural logarithms, labelled subsets. The exact n=10 interior profile has not been inspected; no file or listing in `../oeis-n10/` was accessed. The JSON is the numeric authority.

**Known anchor:** a_20(10)=1,135, ln a_20=7.0343879299, prior work. It is excluded from scoring. The unseen count targets are m=12..19 and maximal targets m=14..19.

**Exposure disclosure:** the required n<=9 report included a Knuth estimate of 7.47 trillion total n=10 safe subsets (SE 0.217 trillion), and the required sampler reports included endpoint diagnostics. These are not fit targets; the registration is blind to exact n=10 profile cells, not to that disclosed total-size estimate. No n=10 MC interior rows were used.

## Two finite forecasting rules

Let B_(n,m) count all labelled subsets with at most two points in each row and column. It is computed exactly by a row/column-degree DP. Let C_n=ln B_(n,2n)-ln a_(2n), using published endpoints. Both models forecast L_m=ln B_(10,m)-C_10*w_m, then apply only deterministic count/ledger bounds.

- **Q — density-scaled quota correction:** transport the normalized oblique cost at the same density m/n from n=9, with linear interpolation.
- **H — fixed-hole terminal correction:** at the same hole count h=2n-m, extrapolate normalized cost as a+b/n from n=6..9.

Both condition on the exact calibration rows through n=9 and the published endpoints through n=20. This reproduces those data by empirical conditioning; it is not an independent derivation of them. Neither model derives component counts. The shared shattering prediction is a separate conjecture based on the exact graph record.

For maximal counts, both use the mean insertion f_m=(m+1)exp(L_(m+1)-L_m) and a binomial menu approximation F~Binomial(h²,f_m/h²). Thus M_m≈exp(L_m)(1-f_m/h²)^(h²). This menu law is **heuristic**. At h=1, F is Bernoulli exactly and M_19=a_19-22,700.

## Point predictions and nominal 80% bands

### Model Q: Density-scaled quota correction

| m | ln a_m | 80% band |
|---:|---:|---:|
| 12 | 28.429242 | [28.079242, 28.779242] |
| 13 | 28.387676 | [27.942973, 28.832378] |
| 14 | 27.840037 | [27.305871, 28.374202] |
| 15 | 26.715980 | [25.923629, 27.508331] |
| 16 | 24.920652 | [23.913776, 25.927529] |
| 17 | 22.320797 | [21.241541, 23.400052] |
| 18 | 18.715592 | [17.601463, 19.829721] |
| 19 | 13.794474 | [12.725489, 14.863459] |
| 20 (known anchor) | 7.034388 | [7.034388, 7.034388] |

| m | Maximal sets, point | 80% band |
|---:|---:|---:|
| 14 | 6,548,354,845 | [3,251,816,779, 13,186,767,300] |
| 15 | 24,130,000,944 | [11,982,603,848, 48,591,854,734] |
| 16 | 17,848,686,293 | [7,184,085,359, 44,344,629,331] |
| 17 | 2,987,554,019 | [1,037,084,487, 8,606,318,113] |
| 18 | 116,640,567 | [32,238,872, 422,006,741] |
| 19 | 956,483 | [313,509, 2,829,094] |

Peak m: **12**, nominal 80% band [11, 13].
First m with extendable fraction <1/2: **17**, nominal 80% band [16, 18].
First disconnected completable layer: **13**, nominal 80% band [12, 15].

The graph feature needs an additional component census and is not part of the primary score.

### Model H: Fixed-hole terminal correction

| m | ln a_m | 80% band |
|---:|---:|---:|
| 12 | 28.899146 | [28.081710, 29.716581] |
| 13 | 28.766732 | [27.866512, 29.666953] |
| 14 | 28.097188 | [27.211069, 28.983306] |
| 15 | 26.826345 | [26.056535, 27.596155] |
| 16 | 24.865205 | [24.221814, 25.508595] |
| 17 | 22.090536 | [21.378292, 22.802781] |
| 18 | 18.324923 | [17.308974, 19.340872] |
| 19 | 13.338875 | [12.082929, 14.594821] |
| 20 (known anchor) | 7.034388 | [7.034388, 7.034388] |

| m | Maximal sets, point | 80% band |
|---:|---:|---:|
| 14 | 18,136,412,619 | [2,647,532,727, 124,239,998,703] |
| 15 | 42,267,958,714 | [5,826,318,852, 306,639,643,125] |
| 16 | 21,007,514,658 | [6,686,042,106, 66,005,517,923] |
| 17 | 2,561,393,179 | [1,271,950,209, 5,158,012,451] |
| 18 | 79,633,866 | [33,514,929, 189,215,750] |
| 19 | 598,169 | [154,127, 2,157,268] |

Peak m: **12**, nominal 80% band [11, 13].
First m with extendable fraction <1/2: **17**, nominal 80% band [16, 18].
First disconnected completable layer: **13**, nominal 80% band [12, 15].

The graph feature needs an additional component census and is not part of the primary score.

## Uncertainty and scoring — fixed before the data

For each target, use errors from rolling conditional forecasts of n=6,7,8,9. Q aligns targets by nearest density (round half up); H aligns by h. Halfwidth=t_3(0.9)*sqrt(1.25)*RMS(signed errors), floored at .35 for ln a and .70 for ln(1+M). Truncate to deterministic bounds; special exact transform at m=19. Peak and half-fraction level use a minimum radius of one. These are nominal 80% predictive bands, with no coverage theorem; four correlated board cases cannot establish calibration.

For each target use IS80=(u-l)+10 max(l-y,0)+10 max(y-u,0), and WIS=[0.5|y-p|+0.1 IS80]/1.5. For count targets y=ln a_m; for maximal targets use y=ln(1+M_m), transforming point and band endpoints as well.

0.5*mean(WIS over 8 unknown ln a targets)+0.5*mean(WIS over 6 ln(1+M) targets); smaller is better. Equal family weight; do not treat cells as independent replicates.

Report MAE and 80% coverage separately for each family. Peak (smallest maximizer if tied) and first e<1/2: absolute error, IS80, and coverage, reported separately. The shattering prediction is unscored unless a separate full completion-support graph census is supplied.

Declare Q or H the finite-forecast winner only if primary scores differ by at least 0.01; otherwise report a tie. No significance claim or asymptotic model selection follows from this single board.

Exact endpoint identities, axis-cap bounds, the known endpoint and low-cardinality combinatorics are conditioned facts, not successful forecasts. The forecasts share correlated errors, and the four retrospective hindcasts were used for model development.

## What the models would mean at infinity

The finite rules alone do not choose an extinction ratio. To make the stakes explicit, the JSON supplies two illustrative continuations beyond n=20: Q keeps a sparse exp(constant*n) endpoint population and tends to ratio 2; H adds an n log n barrier after density 1.25 and tends to pi/sqrt(3). Both match every supplied endpoint and all exact calibration profiles. The closures can be swapped between the finite models without changing those observations. Neither closure is established, and n=10 cannot validate it.

**Freeze rule:** keep this file and its JSON byte-identical. Any later revision must have a new filename and date. Score this version even if a later analysis favours another model.

Full source hashes and executable rules are in `predictions-n10.json`, `models.py`, `anatomy.py`, and `preregister.py`.
