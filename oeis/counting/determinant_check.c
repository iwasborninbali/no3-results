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
static int n, N, chosen[23];
static bits forbidden_pair[121][121], full;
static uint64_t profile[23], maximal[23], visits;
static double started;
static int split_rows=2, shard_id=0, shard_count=1;
static uint64_t frontier_index, assigned_frontiers, freedom_profile[23];
static bits prefix_mask;
static double cpu_now(void) { return (double)clock()/CLOCKS_PER_SEC; }
static int pop(bits b) { return __builtin_popcountll((uint64_t)b)+__builtin_popcountll((uint64_t)(b>>64)); }
static void add_count(uint64_t *dst,uint64_t v) {
    if (UINT64_MAX-*dst<v) { fprintf(stderr,"count overflow\n"); exit(2); }
    *dst+=v;
}

static double now(void) {
    struct timespec t; clock_gettime(CLOCK_MONOTONIC,&t);
    return (double)t.tv_sec+1e-9*(double)t.tv_nsec;
}
static int first(bits b) {
    uint64_t lo=(uint64_t)b;
    return lo?__builtin_ctzll(lo):64+__builtin_ctzll((uint64_t)(b>>64));
}
static void enumerate(bits candidates, bits covered, int k) {
    add_count(&profile[k],1);
    add_count(&freedom_profile[k],pop(full & ~covered));
    if (covered==full) add_count(&maximal[k],1);
    if ((++visits & ((UINT64_C(1)<<28)-1))==0) {
        fprintf(stderr,"PROGRESS n=%d visits=%"PRIu64" seconds=%.3f\n",n,visits,now()-started);
        fprintf(stderr,"CPU_SECONDS %.6f\n",cpu_now());
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
/* Enumerate every legal subset of the prefix cells. Each terminal prefix
 * owns exactly its suffix subsets, including the empty suffix. No nodes are
 * counted by the splitter; hence no small-set correction or overlap exists.
 */
static void split(bits candidates,bits covered,int k) {
    bits early=candidates & prefix_mask;
    if (!early) {
        uint64_t index=frontier_index++;
        if (index % (uint64_t)shard_count != (uint64_t)shard_id) return;
        ++assigned_frontiers;
        enumerate(candidates,covered,k);
        return;
    }
    int p=first(early);
    candidates &= ~((bits)1<<p);
    split(candidates,covered,k);
    bits next_covered=covered|((bits)1<<p);
    for (int j=0;j<k;++j) next_covered |= forbidden_pair[p][chosen[j]];
    chosen[k]=p;
    split(candidates & ~next_covered,next_covered,k+1);
}
int main(int argc,char **argv) {
    if (argc!=5 || (n=atoi(argv[1]))<2 || n>11) { fprintf(stderr,"usage: %s N SHARD SHARDS SPLIT_ROWS (N=2..11)\n",argv[0]); return 2; }
    shard_id=atoi(argv[2]); shard_count=atoi(argv[3]); split_rows=atoi(argv[4]);
    if (shard_count<1 || shard_id<0 || shard_id>=shard_count || split_rows<0 || split_rows>=n) return 2;
    N=n*n; full=((bits)1<<N)-1; started=now();
    prefix_mask=((bits)1<<(split_rows*n))-1;
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
    split(full,0,0);
    uint64_t total=0, max_total=0;
    for (int k=0;k<=2*n;++k) { add_count(&total,profile[k]); add_count(&max_total,maximal[k]); }
    printf("{\"n\":%d,\"total\":%"PRIu64",\"maximal\":%"PRIu64",\"profile\":[",n,total,max_total);
    for (int k=0;k<=2*n;++k) printf("%s%"PRIu64,k?",":"",profile[k]);
    printf("],\"maximal_profile\":[");
    for (int k=0;k<=2*n;++k) printf("%s%"PRIu64,k?",":"",maximal[k]);
    printf("],\"freedom_profile\":[");
    for (int k=0;k<=2*n;++k) printf("%s%"PRIu64,k?",":"",freedom_profile[k]);
    printf("],\"program\":\"det\",\"split_rows\":%d,\"shard\":%d,\"shards\":%d,\"frontiers\":%"PRIu64",\"assigned_frontiers\":%"PRIu64",\"cpu_seconds\":%.6f",
           split_rows,shard_id,shard_count,frontier_index,assigned_frontiers,cpu_now());
    printf(",\"seconds\":%.6f,\"visits\":%"PRIu64"}\n",now()-started,visits);
    fflush(stdout);
    fprintf(stderr,"DONE n=%d seconds=%.6f\n",n,now()-started);
    return 0;
}
