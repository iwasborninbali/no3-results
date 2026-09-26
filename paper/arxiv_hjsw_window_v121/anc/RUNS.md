# v1.21 execution record

All commands were run from `anc/` on 26 September 2026, offline, using "python3 (3.14, with numpy)" (CPython 3.14.6, NumPy 2.5.2, SciPy 1.18.0). Elapsed times are wall-clock seconds per job, including interpreter startup. The commands were `python3 run_all.py` (42 existing jobs) and `python3 run_all.py v121_formulas` after registering the new job. Together these executed every current jobs.json entry through the batch and per-job drivers. `python3 verify_v121.py` also passed directly.

**41 PASS, 2 NOT RUN, 0 FAILED.** NOT RUN has no process exit code and is not counted as success. PySAT remains optional and absent. The completed boxes job also reports its optional PySAT MIP stage as skipped.

Sources, arguments, bounded function calls and dependencies are documented in README.md and jobs.json. Passing finite checks and numerical/model evaluations do not prove BS, BT, CP, PC or UM. Historical records, including the R1-prefixed output files, remain distinct from the fresh output in runs/generated.

| Job | Command | Exit code | Seconds | Status | Output |
|---|---|---|---|---|---|
| saturation | `python3 run_one.py saturation` | 0 | 0.047 | PASS | [runs/saturation.log](runs/saturation.log) |
| window | `python3 run_one.py window` | 0 | 183.331 | PASS | [runs/window.log](runs/window.log) |
| boxes | `python3 run_one.py boxes` | 0 | 227.593 | PASS | [runs/boxes.log](runs/boxes.log) |
| gadget | `python3 run_one.py gadget` | 0 | 14.293 | PASS | [runs/gadget.log](runs/gadget.log) |
| eight_cover | `python3 run_one.py eight_cover` | 0 | 0.738 | PASS | [runs/eight_cover.log](runs/eight_cover.log) |
| block_cover | `python3 run_one.py block_cover` | — | 0.000 | NOT RUN | PySAT is not installed; maxlawful_pysat is imported at module load. |
| km1_lines | `python3 run_one.py km1_lines` | 0 | 0.590 | PASS | [runs/km1_lines.log](runs/km1_lines.log) |
| cycle | `python3 run_one.py cycle` | 0 | 0.575 | PASS | [runs/cycle.log](runs/cycle.log) |
| potential | `python3 run_one.py potential` | 0 | 0.696 | PASS | [runs/potential.log](runs/potential.log) |
| arcs | `python3 run_one.py arcs` | 0 | 0.198 | PASS | [runs/arcs.log](runs/arcs.log) |
| g8 | `python3 run_one.py g8` | 0 | 0.466 | PASS | [runs/g8.log](runs/g8.log) |
| cycles_dependency | `python3 run_one.py cycles_dependency` | 0 | 0.075 | PASS | [runs/cycles_dependency.log](runs/cycles_dependency.log) |
| lp_dependency | `python3 run_one.py lp_dependency` | 0 | 0.908 | PASS | [runs/lp_dependency.log](runs/lp_dependency.log) |
| sat_dependency | `python3 run_one.py sat_dependency` | — | 0.000 | NOT RUN | PySAT is not installed. |
| monomial_integral | `python3 run_one.py monomial_integral` | 0 | 0.939 | PASS | [runs/monomial_integral.log](runs/monomial_integral.log) |
| monomial_cover | `python3 run_one.py monomial_cover` | 0 | 2.189 | PASS | [runs/monomial_cover.log](runs/monomial_cover.log) |
| cubic_cover | `python3 run_one.py cubic_cover` | 0 | 0.857 | PASS | [runs/cubic_cover.log](runs/cubic_cover.log) |
| cubic_lines_3203_0_0 | `python3 run_one.py cubic_lines_3203_0_0` | 0 | 0.533 | PASS | [runs/cubic_lines_3203_0_0.log](runs/cubic_lines_3203_0_0.log) |
| cubic_lines_3203_700_-2100 | `python3 run_one.py cubic_lines_3203_700_-2100` | 0 | 0.509 | PASS | [runs/cubic_lines_3203_700_-2100.log](runs/cubic_lines_3203_700_-2100.log) |
| cubic_lines_12809_0_0 | `python3 run_one.py cubic_lines_12809_0_0` | 0 | 1.623 | PASS | [runs/cubic_lines_12809_0_0.log](runs/cubic_lines_12809_0_0.log) |
| cubic_lines_12809_-6404_0 | `python3 run_one.py cubic_lines_12809_-6404_0` | 0 | 1.679 | PASS | [runs/cubic_lines_12809_-6404_0.log](runs/cubic_lines_12809_-6404_0.log) |
| components | `python3 run_one.py components` | 0 | 0.080 | PASS | [runs/components.log](runs/components.log) |
| mirrored | `python3 run_one.py mirrored` | 0 | 0.794 | PASS | [runs/mirrored.log](runs/mirrored.log) |
| signature_sample | `python3 run_one.py signature_sample` | 0 | 4.078 | PASS | [runs/signature_sample.log](runs/signature_sample.log) |
| old_constant | `python3 run_one.py old_constant` | 0 | 2.557 | PASS | [runs/old_constant.log](runs/old_constant.log) |
| orbit_stability | `python3 run_one.py orbit_stability` | 0 | 4.393 | PASS | [runs/orbit_stability.log](runs/orbit_stability.log) |
| orbit_types | `python3 run_one.py orbit_types` | 0 | 2.437 | PASS | [runs/orbit_types.log](runs/orbit_types.log) |
| standard_model | `python3 run_one.py standard_model` | 0 | 8.289 | PASS | [runs/standard_model.log](runs/standard_model.log) |
| constant2 | `python3 run_one.py constant2` | 0 | 0.087 | PASS | [runs/constant2.log](runs/constant2.log) |
| old_block_constant | `python3 run_one.py old_block_constant` | 0 | 0.078 | PASS | [runs/old_block_constant.log](runs/old_block_constant.log) |
| fast_blocks | `python3 run_one.py fast_blocks` | 0 | 2.826 | PASS | [runs/fast_blocks.log](runs/fast_blocks.log) |
| clean | `python3 run_one.py clean` | 0 | 4.711 | PASS | [runs/clean.log](runs/clean.log) |
| seven_cover | `python3 run_one.py seven_cover` | 0 | 6.891 | PASS | [runs/seven_cover.log](runs/seven_cover.log) |
| U | `python3 run_one.py U` | 0 | 50.000 | PASS | [runs/U.log](runs/U.log) |
| U_validation | `python3 run_one.py U_validation` | 0 | 0.240 | PASS | [runs/U_validation.log](runs/U_validation.log) |
| gamma1 | `python3 run_one.py gamma1` | 0 | 5.755 | PASS | [runs/gamma1.log](runs/gamma1.log) |
| gamma2_hybrid | `python3 run_one.py gamma2_hybrid` | 0 | 0.416 | PASS | [runs/gamma2_hybrid.log](runs/gamma2_hybrid.log) |
| gamma2_continuum | `python3 run_one.py gamma2_continuum` | 0 | 5.175 | PASS | [runs/gamma2_continuum.log](runs/gamma2_continuum.log) |
| independent_constants | `python3 run_one.py independent_constants` | 0 | 1.384 | PASS | [runs/independent_constants.log](runs/independent_constants.log) |
| independent_core | `python3 run_one.py independent_core` | 0 | 0.458 | PASS | [runs/independent_core.log](runs/independent_core.log) |
| arithmetic_library | `python3 run_one.py arithmetic_library` | 0 | 0.078 | PASS | [runs/arithmetic_library.log](runs/arithmetic_library.log) |
| v120_formulas | `python3 run_one.py v120_formulas` | 0 | 0.191 | PASS | [runs/v120_formulas.log](runs/v120_formulas.log) |
| v121_formulas | `python3 run_one.py v121_formulas` | 0 | 0.372 | PASS | [runs/v121_formulas.log](runs/v121_formulas.log) |

## Key output lines

### saturation

```text
rejected: ValueError vibes: it fits
rejected: ValueError a frontier with content is a submission, not a fact
rejected: NotImplementedError n=101: your end
```

### window

```text
p=101 c=  2: |P|= 400  lines>=3:  150 (all slope ±1)  Z= 0  2|L|+Z= 300=3(p-1)  exact max= 300 (witness lawful)  #max subsets=1=9^0
p=101 c=100: |P|= 400  lines>=3:  148 (all slope ±1)  Z= 4  2|L|+Z= 300=3(p-1)  exact max= 300 (witness lawful)  #max subsets=81=9^2
all checks passed
```

### boxes

```text
5. p=13: per-orbit maxima/counts by pattern (brute force) = exc 6 (9|6), (0,0) 8 (1296), (1,1) 10 (144), (0,2)/(2,0) 12 (1) for all c, boxes
6. MIP cross-check SKIPPED — missing dependency: pysat (needs numpy, scipy>=1.9 and python-sat for maxlawful_pysat.lines)
all checks passed
```

### gadget

```text
p=11: ok, (1,1)-orbits checked so far: 67
p=13: ok, (1,1)-orbits checked so far: 129
ALL OK: every (1,1) orbit has the stated line structure, maximum 10, and 9/54/81 maximum sets by t
```

### eight_cover

```text
p=23: m8=2, blocks=4, cover cost = 80 = 4(p-1) - 4 m8 = 80  (3.636(p-1)); LP(1) = 80.00
p=31: m8=2, blocks=4, cover cost = 112 = 4(p-1) - 4 m8 = 112  (3.733(p-1)); LP(1) = 108.00
p=101: m8=8, blocks=16, cover cost = 368 = 4(p-1) - 4 m8 = 368  (3.680(p-1)); LP(1) = 353.33
```

### block_cover

```text
PySAT is not installed; maxlawful_pysat is imported at module load.
```

### km1_lines

```text
1489: 5:118 6:262 7:114 8:108   8/p=0.073  (>=5 total 602, /p=0.404)
1493: 5:128 6:242 7:128 8:120   8/p=0.080  (>=5 total 618, /p=0.414)
1499: 5:118 6:268 7:118 8:122   8/p=0.081  (>=5 total 626, /p=0.418)
```

### cycle

```text
   all t=1: saving -60.00 (formula 2*changes-6*G8 = -60); all t=1/2: saving 2.00
   synthetic seed 0: LP saving 15.86 (net/group 0.466)
   synthetic seed 1: LP saving 21.40 (net/group 0.629)
```

### potential

```text
p=199 k=3: G8=34 cycles=1 R=4 sum|A-B|=0 -> saving 17.00 => alpha <= 775.00 = 3.9141(p-1); LP(t=1/R) net 17.00
p=401 k=3: G8=58 cycles=1 R=6 sum|A-B|=0 -> saving 19.33 => alpha <= 1580.67 = 3.9517(p-1); LP(t=1/R) net 19.33
p=401 k=5: G8=48 cycles=16 R=9 sum|A-B|=48 -> saving 0.00 => alpha <= 1600.00 = 4.0000(p-1); LP(t=1/R) net -0.00
```

### arcs

```text
p=1009 g=11: |K|=|M|=332  max_m|S_K|/sqrt p=2.24  max|S_M|/sqrt p=2.49  max|S_D|/sqrt p=3.25  (log p=6.9)  max arc |imbalance|=14 = 0.44 sqrt p
p=2003 g=5: |K|=|M|=668  max_m|S_K|/sqrt p=2.16  max|S_M|/sqrt p=2.20  max|S_D|/sqrt p=3.18  (log p=7.6)  max arc |imbalance|=22 = 0.49 sqrt p
p=4001 g=3: |K|=|M|=1360  max_m|S_K|/sqrt p=2.50  max|S_M|/sqrt p=2.26  max|S_D|/sqrt p=3.41  (log p=8.3)  max arc |imbalance|=49 = 0.77 sqrt p
```

### g8

```text
k=3: G8/p over primes 100..500: mean 0.1631 min 0.0917 max 0.2211 (n=70); 4-class groups/p mean 0.488; both-shared fraction 0.336; sample: [(101, 10), (199, 34), (401, 58), (499, 74)]
k=5: G8/p over primes 100..500: mean 0.1598 min 0.0734 max 0.2199 (n=70); 4-class groups/p mean 0.484; both-shared fraction 0.334; sample: [(101, 16), (199, 30), (401, 48), (499, 84)]
k=7: G8/p over primes 100..500: mean 0.1642 min 0.1069 max 0.2011 (n=70); 4-class groups/p mean 0.492; both-shared fraction 0.332; sample: [(101, 18), (199, 28), (401, 54), (499, 78)]
```

### cycles_dependency

```text
89 3 88 | 28 28 | 20 | 2 | 0.21 | 0.136 0.182 0.182 0.500
97 5 96 | 28 28 | 14 | 4 | 0.41 | 0.104 0.188 0.188 0.521
101 2 100 | 32 32 | 12 | 10 | 1.00 | 0.060 0.260 0.260 0.420
```

### lp_dependency

```text
p=101 poly:1,0,0,0 box=(0,0) N=2p=202 pts=404
  pm1: lines>=3: 91 sizes={3: 46, 4: 11, 5: 11, 6: 23} LP=266.00 = 1.317 N = 2.634 p
  all: lines>=3: 1517 sizes={3: 1472, 4: 11, 5: 11, 6: 23} LP=221.82 = 1.098 N = 2.196 p
```

### sat_dependency

```text
PySAT is not installed.
```

### monomial_integral

```text
k=7: L/p=877/1680 U/p=9582277/5443200 C_k=15265237/5443200 = 2.804460060
k=9: L/p=237017/453600 U/p=59007510811/33530112000 C_k=94048104091/33530112000 = 2.804884878
k=11: L/p=62574389/119750400 U/p=397658627087627/225966130790400 C_k=126762273520591/45193226158080 = 2.804895430
```

### monomial_cover

```text
p=10000019 k=5 box=(0,0): L/p=0.51658 U/p=1.76306 cost/p=2.79623 = 1.39812 N
```

### cubic_cover

```text
p=197 a=1 box=(-98,-98): L4=92 sizes={4: 26, 5: 26, 6: 40} covered=440/788 cost=532 = 1.350 N
p=197 a=1 box=(79,-190): L4=103 sizes={4: 37, 5: 37, 6: 29} covered=455/788 cost=539 = 1.368 N
p=197 a=1 box=(-130,-114): L4=97 sizes={4: 31, 5: 31, 6: 35} covered=448/788 cost=534 = 1.355 N
```

### cubic_lines_3203_0_0

```text
  family j<=5: good=422 (0.1318p) pairs=68 (0.0212p) |good|-pairs=0.1105p  Caro-Wei=0.1122p  greedy=0.1136p -> cost(greedy)=1.3213 N
  family j<=6: good=422 (0.1318p) pairs=68 (0.0212p) |good|-pairs=0.1105p  Caro-Wei=0.1122p  greedy=0.1136p -> cost(greedy)=1.3213 N
  family j<=8: good=422 (0.1318p) pairs=68 (0.0212p) |good|-pairs=0.1105p  Caro-Wei=0.1122p  greedy=0.1136p -> cost(greedy)=1.3213 N
```

### cubic_lines_3203_700_-2100

```text
  family j<=5: good=429 (0.1339p) pairs=81 (0.0253p) |good|-pairs=0.1086p  Caro-Wei=0.1120p  greedy=0.1146p -> cost(greedy)=1.3121 N
  family j<=6: good=429 (0.1339p) pairs=81 (0.0253p) |good|-pairs=0.1086p  Caro-Wei=0.1120p  greedy=0.1146p -> cost(greedy)=1.3121 N
  family j<=8: good=429 (0.1339p) pairs=81 (0.0253p) |good|-pairs=0.1086p  Caro-Wei=0.1120p  greedy=0.1146p -> cost(greedy)=1.3121 N
```

### cubic_lines_12809_0_0

```text
  family j<=5: good=1682 (0.1313p) pairs=352 (0.0275p) |good|-pairs=0.1038p  Caro-Wei=0.1072p  greedy=0.1101p -> cost(greedy)=1.3206 N
  family j<=6: good=1682 (0.1313p) pairs=352 (0.0275p) |good|-pairs=0.1038p  Caro-Wei=0.1072p  greedy=0.1101p -> cost(greedy)=1.3206 N
  family j<=8: good=1682 (0.1313p) pairs=352 (0.0275p) |good|-pairs=0.1038p  Caro-Wei=0.1072p  greedy=0.1101p -> cost(greedy)=1.3206 N
```

### cubic_lines_12809_-6404_0

```text
  family j<=5: good=1748 (0.1365p) pairs=404 (0.0315p) |good|-pairs=0.1049p  Caro-Wei=0.1089p  greedy=0.1120p -> cost(greedy)=1.3188 N
  family j<=6: good=1748 (0.1365p) pairs=404 (0.0315p) |good|-pairs=0.1049p  Caro-Wei=0.1089p  greedy=0.1120p -> cost(greedy)=1.3188 N
  family j<=8: good=1748 (0.1365p) pairs=404 (0.0315p) |good|-pairs=0.1049p  Caro-Wei=0.1089p  greedy=0.1120p -> cost(greedy)=1.3188 N
```

### components

```text
p=4001 k=  3: vertices 2001, edges 2001, components 380, largest 32 (1.6% of vertices), small sizes {1: 118, 2: 34, 3: 36, 4: 34, 5: 28, 6: 24}
p=4001 k=  5: vertices 2001, edges 2002, components 312, largest 95 (4.7% of vertices), small sizes {1: 108, 2: 42, 3: 26, 4: 26, 5: 8, 6: 16}
p=4001 k=  7: vertices 2001, edges 2002, components 293, largest 177 (8.8% of vertices), small sizes {1: 120, 2: 38, 3: 34, 4: 23, 5: 12, 6: 6}
```

### mirrored

```text
p=17: orbits 5; (|O| pts, max in O, max in O∪R(O)) -> count: {(8, 6, 8): 2, (16, 12, 16): 3}; sum over orbits: H(1) alone 48 (=3(p-1)=48), unions 64 = 4.000(p-1)
p=19: orbits 5; (|O| pts, max in O, max in O∪R(O)) -> count: {(8, 6, 8): 1, (16, 12, 16): 4}; sum over orbits: H(1) alone 54 (=3(p-1)=54), unions 72 = 4.000(p-1)
p=23: orbits 6; (|O| pts, max in O, max in O∪R(O)) -> count: {(8, 6, 8): 1, (16, 12, 16): 5}; sum over orbits: H(1) alone 66 (=3(p-1)=66), unions 88 = 4.000(p-1)
```

### signature_sample

```text
  10100      k=6 saving= 17.00 count=1
  11000      k=6 saving= 16.00 count=1
written runs/generated/sig_savings.json
```

### old_constant

```text
K=8: saving/p = 2778667/5160960 = 0.538401   =>   alpha <= 17865173/5160960 = 3.4616 (p-1)
tail (k>K, sav <= 4(k-1)) <= 0.0352
```

### orbit_stability

```text
p=29 orbit type (classes=4, points=16): count=6 opt={12} #optimal patterns={1} stability c(d)={((1, 1), (2, 2), (3, 3))}
p=31 orbit type (classes=2, points=8): count=1 opt={6} #optimal patterns={9} stability c(d)={((1, 0), (2, 0), (3, 0))}
p=31 orbit type (classes=4, points=16): count=7 opt={12} #optimal patterns={1} stability c(d)={((1, 1), (2, 2), (3, 3))}
```

### orbit_types

```text
orbit incidence types found: 2
  classes=2 points=8 richline profile=(3, 3): n=14 (p=[3, 5, 7, 11, 13, 17, 19, 23, 29, 31]) -> (opt,#max,c(d))={(6, 9, ((1, 0), (2, 0)))}
  classes=4 points=16 richline profile=(4, 4, 3, 3, 3, 3): n=30 (p=[7, 11, 13, 17, 19, 23, 29, 31]) -> (opt,#max,c(d))={(12, 1, ((1, 1), (2, 2)))}
```

### standard_model

```text
  xi=1101      -> [(12.0, 128)]
  xi=1110      -> [(12.0, 128)]
  xi=1111      -> [(10.0, 128)]
```

### constant2

```text
K=9: saving/p >= 0.55183 (untabulated density 0.00e+00)  =>  alpha <= 3.4482(p-1)
tail (k>9) <= 0.01953  =>  certificate constant in [3.4286, 3.4482]
```

### old_block_constant

```text
  k=8: contribution=0.02284  (density of signatures missing from the table: 0.000000)
saving/p (k<=8) = 0.5384  =>  alpha <= 3.4616 (p-1)
tail bound (k>8, using sav <= 4(k-1)): 0.0352  =>  full constant in [3.4264, 3.4616]
```

### fast_blocks

```text
  a7677a     sav= 16.00 count=1
  a67787b    sav= 18.00 count=1
  a767868b   sav= 25.00 count=1
```

### clean

```text
wrote anc/slack/t221_agents/clean_counts_output.txt  (405 main rows + 5 extension rows, 37 LP(1) rows)  total time 4.59s
```

### seven_cover

```text
p= 499  n_pts= 3984  m8= 40 m7= 34 m6groups= 50  orbits= 17 LP=28: 17 exc= 0  (0.18s)
# total elapsed 6.3s
wrote slack/t221_agents/orbit_cover_output.txt and orbit_cover_detail.json
```

### U

```text
(d,e)=(0, 1): max|exact-MC|=0.0305 mean|.|=0.00621  (MC noise ~ 1/sqrt(M)=0.0158)
(d,e)=(1, 0): max|exact-MC|=0.0323 mean|.|=0.00625  (MC noise ~ 1/sqrt(M)=0.0158)
(d,e)=(1, 1): max|exact-MC|=0.0347 mean|.|=0.00614  (MC noise ~ 1/sqrt(M)=0.0158)
```

### U_validation

```text
  lift (1,1): cells(n>=5)=191  mean z=-0.028  std z=1.072  frac|z|>2=0.042  frac|z|>3=0.000  (pure noise expects mean~0,std~1,frac>2~0.05,frac>3~0.003)
    U-decile calib (10 bins, ~320 residues/bin): max|pred-emp|=0.0719  table(pred,emp,n)=(0.267,0.281,320),(0.310,0.316,320),(0.371,0.366,320),(0.432,0.433,321),(0.476,0.459,320),(0.500,0.453,320),(0.500,0.517,321),(0.500,0.428,320),(0.500,0.547,320),(0.500,0.514,321)
WROTE slack/verification/g39_U_validation.txt
```

### gamma1

```text
box 0 0 gamma1 0.12868909349286156
box 0.500039035053478 0 gamma1 0.13609756703956127
box 0.21854511395566656 0.3443646581330003 gamma1 0.13634558976792754
```

### gamma2_hybrid

```text
  p12809_box-6404_0: p=12809  empirical pairs/p = 0.0315   model gamma2 = 0.0304   diff/p = -0.0012
  p3203_box700_-2100: p=3203  empirical pairs/p = 0.0253   model gamma2 = 0.0300   diff/p = +0.0047
log written to slack/verification/g39_gamma2.txt
```

### gamma2_continuum

```text
all ordered configurations {(1, 2): np.float64(0.008261701500495355), (1, 3): np.float64(0.008346424534642575), (2, 1): np.float64(0.008173321170607682), (2, 3): np.float64(0.009224325932040785), (3, 1): np.float64(0.007678603056077736), (3, 2): np.float64(0.009745895420622156)}
unordered gamma2 0.02583245196717871
```

### independent_constants

```text
  ],
  "limits": "Arithmetic conditional on the supplied block savings and stated local-law integrands; does not prove either model."
}
```

### independent_core

```text
    }
  ]
}
```

### arithmetic_library

```text
{'k': 3, 'L': '1/2', 'U': '7/4', 'C': '11/4', 'C_decimal': 2.75}
```

### v120_formulas

```text
Exact p=5 cubic maximum: 12; no lawful 13-subset. Witness: [(-2, 2), (-2, 7), (-1, 4), (-1, 9), (0, 0), (1, 1), (1, 6), (2, 3), (2, 8), (3, 7), (6, 1), (7, 8)]
FE conic 101 points 102 = p - chi(-3)
FE conic 1009 points 1008 = p - chi(-3)
FE conic 1013 points 1014 = p - chi(-3)
Corrected direction formula: all u, p=101,107; a=1,2; families (1,3),(2,3).
Pair configuration 1 2 ratio 4 coefficients ['-1', '-16', '-4', '20', '5']
Pair configuration 1 3 ratio -4/5 coefficients ['-1', '-4', '16/5', '4/5', '5']
Pair configuration 2 3 ratio -1/5 coefficients ['-1', '-4', '1/5', '4/5', '5']
Exact tail 5/256 = 0.01953125 margin/discrepancy 110/51 = 2.156862745098039
Coefficients: 663/250 2657/1000
C11 plus twice the convergence error and the full-split correction < 2.81: exact rational check passed.
ALL v1.20 checks passed
```

### v121_formulas

```text
F1: p=11, c=1: [0,23)^2 and [0,22)^2 have the same 40 points; exact maximum 22 < 30.
F1: 68 exact HJSW maxima, all nonzero c at primes 3..19; lawful witnesses retained in 204 containing squares.
F2: p=23, a=1, B=[0,46)^2: L4=11+2=13; U=42-6=36.
F2: p=11 positive slope: same=1, split=0; finite split proportion is not 1/2.
F2: corrected exact L4 and U formulas match direct enumeration in 896 cases at eight primes, every a and four boxes; corrections bounded by 4 lines and 16 points.
F4: p=11 base copies (2,6),(5,9): common centre -4; first coordinates have the same sign.
F4: 146 base-pair checks and 82115 torus points at nine primes; corrected symmetry preserves relation and swaps sharing events; 115/32 unchanged.
ALL v1.21 checks passed
```

## Portable records and integrity

Only the newly printed absolute ancillary-directory prefix in `runs/clean.log` was replaced by `anc/`; its numbers and timing are unchanged. All other recorded commands already use `python3` and relative paths. The source scripts and archived input data were retained unchanged. `MANIFEST.sha256` was regenerated after this complete run and documentation update; it covers all ancillary files except itself. The final verification and archive details are in the external `CHANGES-v121.md`.
