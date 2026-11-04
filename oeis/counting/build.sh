#!/bin/sh
set -eu
cd "$(dirname "$0")"
gcc -O3 -march=native -std=c11 -Wall -Wextra line_rows.c -o line_rows
gcc -O3 -march=native -std=c11 -Wall -Wextra determinant_check.c -o determinant_check
gcc -O3 -march=native -std=c11 -Wall -Wextra tree_estimate.c -lm -o tree_estimate
