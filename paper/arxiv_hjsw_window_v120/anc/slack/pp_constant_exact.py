"""v1.20 portable exact model integral; upstream SymPy implementation is in upstream/.
Uses R1's independently written rational-polynomial integrator, with the same four regions.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'independent'))
from model_arithmetic import constant
for k in map(int, sys.argv[1:]):
    r = constant(k)
    print(f"k={k}: L/p={r['L']} U/p={r['U']} C_k={r['C']} = {r['C_decimal']:.9f}")
