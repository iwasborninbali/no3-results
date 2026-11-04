/* Additional cross-check based on the independent September 10 tri.c
 * (Conductor) in the OEIS archive, extended here to 100 cells.
 * Exact integer determinants, point-by-point subset traversal; no primitive
 * directions, row completion, or symmetry weighting. No freedom-scales code
 * was consulted. In this implementation the remaining candidates are stored
 * as a bitset to avoid scanning already forbidden cells.
 * Compile: gcc -O3 -march=native -std=c11 -Wall -Wextra determinant_check.c -o determinant_check
 */
#define _POSIX_C_SOURCE 200809L
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <inttypes.h>
#include <time.h>
typedef unsigned __int128 bits;
static int n, N, chosen[21];
static bits forbidden_pair[100][100], full;
static uint64_t profile[21], maximal[21], visits;
static double started;
static double now(void) {
    struct timespec t; clock_gettime(CLOCK_MONOTONIC,&t);
    return (double)t.tv_sec+1e-9*(double)t.tv_nsec;
}
static int first(bits b) {
    uint64_t lo=(uint64_t)b;
    return lo?__builtin_ctzll(lo):64+__builtin_ctzll((uint64_t)(b>>64));
}
static void enumerate(bits candidates, bits covered, int k) {
    ++profile[k];
    if (covered==full) ++maximal[k];
    if ((++visits & ((UINT64_C(1)<<28)-1))==0) {
        fprintf(stderr,"PROGRESS n=%d visits=%"PRIu64" seconds=%.3f\n",n,visits,now()-started);
        fflush(stderr);
    }
    while (candidates) {
        int p=first(candidates); candidates &= candidates-1;
        bits next_covered=covered|((bits)1<<p);
        for (int j=0;j<k;++j) next_covered |= forbidden_pair[p][chosen[j]];
        chosen[k]=p;
        enumerate(candidates & ~next_covered,next_covered,k+1);
    }
}
int main(int argc,char **argv) {
    if (argc!=2 || (n=atoi(argv[1]))<1 || n>10) { fprintf(stderr,"usage: %s N (1..10)\n",argv[0]); return 2; }
    N=n*n; full=((bits)1<<N)-1; started=now();
    for (int a=0;a<N;++a) for (int b=a+1;b<N;++b) {
        bits m=0;
        int ax=a%n, ay=a/n, bx=b%n, by=b/n;
        for (int c=0;c<N;++c) {
            if (c==a || c==b) continue;
            int cx=c%n, cy=c/n;
            if ((bx-ax)*(cy-ay)==(by-ay)*(cx-ax)) m |= (bits)1<<c;
        }
        forbidden_pair[a][b]=forbidden_pair[b][a]=m;
    }
    fprintf(stderr,"START n=%d full determinant traversal, no symmetry\n",n); fflush(stderr);
    enumerate(full,0,0);
    uint64_t total=0, max_total=0;
    for (int k=0;k<=2*n;++k) { total+=profile[k]; max_total+=maximal[k]; }
    printf("{\"n\":%d,\"total\":%"PRIu64",\"maximal\":%"PRIu64",\"profile\":[",n,total,max_total);
    for (int k=0;k<=2*n;++k) printf("%s%"PRIu64,k?",":"",profile[k]);
    printf("],\"maximal_profile\":[");
    for (int k=0;k<=2*n;++k) printf("%s%"PRIu64,k?",":"",maximal[k]);
    printf("],\"seconds\":%.6f,\"visits\":%"PRIu64"}\n",now()-started,visits);
    fflush(stdout);
    fprintf(stderr,"DONE n=%d seconds=%.6f\n",n,now()-started);
    return 0;
}
