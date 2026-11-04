/* Independent exhaustive no-three-in-line enumeration, 2026-11-03.
 * Written from the definition; no freedom-scales source was consulted.
 *
 * Generate maximal lattice lines with >=3 points by primitive directions.
 * A legal set occupies each such line at most twice. Search by rows, choosing
 * zero, one or two points per row, with reversible line-occupancy counters.
 * Complete the last row analytically: if m cells are individually admissible,
 * exactly 1, m, binom(m,2) completions have zero, one, two points in that row.
 * Maximality is tested against ALL grid cells, including earlier omitted ones.
 *
 * Default: reduce by reflection in the vertical axis, using the first nonempty
 * prefix row. Asymmetric first-row patterns have weight 2; symmetric ones
 * retain weight 1 and their entire suffix is searched. --no-sym disables it.
 * --reverse reverses the order of prefix rows (last row stays the tail).
 * --tail-first makes row 0 the analytically completed row instead.
 * Counts fit uint64_t for the attempted sizes; additions are checked.
 * GCC/Clang, C11 plus unsigned __int128. Single-threaded, n <= 10.
 * Example: gcc -O3 -march=native -std=c11 -Wall -Wextra line_rows.c -o line_rows
 *          ./line_rows 8
 */
#define _POSIX_C_SOURCE 200809L
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <inttypes.h>
#include <string.h>
#include <time.h>
#include <assert.h>

typedef unsigned __int128 bits;
#define MAX_N 11
#define MAX_P (MAX_N * MAX_N)
#define MAX_LINES 4096
#define MAX_INC 128
static int n, N, nl, tail, reverse_rows, symmetry = 1;
static bits full, rowmask[MAX_N], line[MAX_LINES];
static bits pairline[MAX_P][MAX_P];
static int incidence[MAX_P][MAX_INC], degree[MAX_P];
static unsigned char occupied[MAX_LINES];
static bits effects[2 * MAX_N + 1][MAX_N];
static uint64_t profile[2 * MAX_N + 1], maximal[2 * MAX_N + 1];
static uint64_t prefix_leaves, row_nodes[MAX_N + 1];
static int roworder[MAX_N];
static double started;
static int split_rows=2, shard_id=0, shard_count=1;
static uint64_t frontier_index, assigned_frontiers;
static uint64_t freedom_profile[2 * MAX_N + 1];
static double cpu_now(void) { return (double)clock()/CLOCKS_PER_SEC; }


static double now(void) {
    struct timespec t;
    if (clock_gettime(CLOCK_MONOTONIC, &t)) { perror("clock_gettime"); exit(1); }
    return (double)t.tv_sec + 1e-9 * (double)t.tv_nsec;
}
static bits bit(int p) { return (bits)1 << p; }
static int pop(bits b) {
    return __builtin_popcountll((uint64_t)b) +
           __builtin_popcountll((uint64_t)(b >> 64));
}
static int first(bits b) {
    uint64_t lo = (uint64_t)b;
    assert(b);
    return lo ? __builtin_ctzll(lo) : 64 + __builtin_ctzll((uint64_t)(b >> 64));
}
static int gcd_int(int a, int b) {
    if (a < 0) a = -a;
    if (b < 0) b = -b;
    while (b) { int t = a % b; a = b; b = t; }
    return a;
}
static int inside(int x, int y) { return x >= 0 && x < n && y >= 0 && y < n; }
static void add_count(uint64_t *dst, uint64_t value) {
    if (UINT64_MAX - *dst < value) { fprintf(stderr, "count overflow\n"); exit(2); }
    *dst += value;
}

/* Each unoriented primitive direction occurs once (dx>0, or dx=0,dy=1).
 * A starting point has no predecessor inside the grid. Consequently each
 * maximal grid line occurs exactly once, with no determinant computation.
 */
static void build_lines(void) {
    full = (bit(N) - 1);
    for (int y = 0; y < n; ++y)
        for (int x = 0; x < n; ++x) rowmask[y] |= bit(y*n+x);
    for (int dx = 0; dx < n; ++dx) {
        for (int dy = -(n-1); dy < n; ++dy) {
            if (dx == 0 && dy != 1) continue;
            if (gcd_int(dx, dy) != 1) continue;
            for (int y = 0; y < n; ++y) for (int x = 0; x < n; ++x) {
                if (inside(x-dx, y-dy)) continue;
                int pts[MAX_N], count = 0;
                bits mask = 0;
                for (int xx=x, yy=y; inside(xx,yy); xx+=dx, yy+=dy) {
                    int p = yy*n+xx;
                    pts[count++] = p; mask |= bit(p);
                }
                if (count < 3) continue;
                if (nl == MAX_LINES) { fprintf(stderr,"too many lines\n"); exit(2); }
                line[nl] = mask;
                for (int i = 0; i < count; ++i) {
                    int p = pts[i];
                    if (degree[p] == MAX_INC) { fprintf(stderr,"too many incidences\n"); exit(2); }
                    incidence[p][degree[p]++] = nl;
                    for (int j = 0; j < count; ++j) if (i != j) {
                        assert(pairline[p][pts[j]] == 0);
                        pairline[p][pts[j]] = mask;
                    }
                }
                ++nl;
            }
        }
    }
}

/* covered = chosen points union all saturated lines. */
static bits put(int p, int k, bits covered) {
    assert(!(covered & bit(p)));
    covered |= bit(p);
    for (int i = 0; i < degree[p]; ++i) {
        int l = incidence[p][i];
        assert(occupied[l] < 2);
        if (occupied[l]++ == 1) covered |= line[l];
    }
    /* effects[k][x]: cells covered by pairing tail point x with the current
     * prefix points. This does not assert that tail point x is admissible. */
    for (int x = 0; x < n; ++x)
        effects[k+1][x] = effects[k][x] | pairline[p][tail*n+x];
    return covered;
}
static void take_back(int p) {
    for (int i = 0; i < degree[p]; ++i) --occupied[incidence[p][i]];
}

static int reflect_pattern(unsigned m) {
    unsigned r = 0;
    for (int x = 0; x < n; ++x) if (m & (1U << x)) r |= 1U << (n-1-x);
    return (int)r;
}
/* Return 0 for the discarded reflection, otherwise the orbit weight. */
static unsigned pattern_weight(unsigned m, int first_row, unsigned weight) {
    if (!symmetry || !first_row) return weight;
    unsigned r = (unsigned)reflect_pattern(m);
    return m > r ? 0 : (m == r ? 1 : 2);
}

static void finish(int k, bits covered, unsigned weight) {
    ++prefix_leaves;
    if ((prefix_leaves & ((UINT64_C(1) << 22) - 1)) == 0) {
        fprintf(stderr,"PROGRESS n=%d prefix_leaves=%"PRIu64" seconds=%.3f\n",n,prefix_leaves,now()-started);
        fprintf(stderr,"CPU_SECONDS %.6f\n",cpu_now());
        fflush(stderr);
    }
    bits available = full & ~covered;
    bits a = available & rowmask[tail];
    unsigned m = (unsigned)pop(a);
    add_count(&profile[k], weight);
    add_count(&profile[k+1], (uint64_t)weight * m);
    add_count(&profile[k+2], m < 2 ? 0 : (uint64_t)weight * m * (m-1) / 2);
    add_count(&freedom_profile[k], (uint64_t)weight * pop(available));
    bits singles=a;
    while (singles) {
        int p=first(singles); singles &= singles-1;
        add_count(&freedom_profile[k+1], (uint64_t)weight *
                  pop(available & ~(effects[k][p%n] | bit(p))));
    }
    if (!available) add_count(&maximal[k], weight);
    if (m == 1) {
        int p = first(a), x = p % n;
        if (!(available & ~(effects[k][x] | bit(p))))
            add_count(&maximal[k+1], weight);
    }
    /* Two tail points saturate their row. For n=2 they select that entire
     * row; the same mask test applies. No third prefix point lies in it. */
    bits earlier = available & ~rowmask[tail];
    while (a) {
        int p = first(a), x = p % n; a &= a-1;
        bits uncovered = earlier & ~effects[k][x];
        bits b = a;
        while (b) {
            int q = first(b); b &= b-1;
            add_count(&freedom_profile[k+2], (uint64_t)weight *
                      pop(uncovered & ~effects[k][q % n]));
            if (!(uncovered & ~effects[k][q % n]))
                add_count(&maximal[k+2], weight);
        }
    }
}

static void search_rows(int r, int k, bits covered, unsigned weight, int first_row) {
    if (r == split_rows) {
        uint64_t index=frontier_index++;
        if (index % (uint64_t)shard_count != (uint64_t)shard_id) return;
        ++assigned_frontiers;
    }
    /* The common top tree belongs to shard 0 in the node-count ledger. */
    if (r >= split_rows || shard_id == 0) ++row_nodes[r];
    if (r == n-1) { finish(k, covered, weight); return; }
    int y = roworder[r];
    search_rows(r+1, k, covered, weight, first_row); /* empty row */
    bits a = rowmask[y] & ~covered;
    while (a) {
        int p = first(a); a &= a-1;
        bits c = put(p, k, covered);
        unsigned pattern = 1U << (p % n);
        unsigned w = pattern_weight(pattern, first_row, weight);
        if (w) search_rows(r+1, k+1, c, w, 0);
        bits b = a & ~c;
        while (b) {
            int q = first(b); b &= b-1;
            w = pattern_weight(pattern | (1U << (q % n)), first_row, weight);
            if (!w) continue;
            bits d = put(q, k+1, c);
            search_rows(r+1, k+2, d, w, 0);
            take_back(q);
        }
        take_back(p);
    }
}

int main(int argc, char **argv) {
    if (argc < 2) { fprintf(stderr,"usage: %s N [--no-sym] [--reverse] [--tail-first]\n",argv[0]); return 2; }
    n = atoi(argv[1]);
    if (n < 1 || n > MAX_N) { fprintf(stderr,"N must be 1..%d\n",MAX_N); return 2; }
    tail = n-1;
    for (int i=2; i<argc; ++i) {
        if (!strcmp(argv[i],"--split-rows") && i+1<argc) split_rows=atoi(argv[++i]);
        else if (!strcmp(argv[i],"--shard") && i+1<argc) shard_id=atoi(argv[++i]);
        else if (!strcmp(argv[i],"--shards") && i+1<argc) shard_count=atoi(argv[++i]);
        else if (!strcmp(argv[i],"--no-sym")) symmetry=0;
        else if (!strcmp(argv[i],"--reverse")) reverse_rows=1;
        else if (!strcmp(argv[i],"--tail-first")) tail=0;
        else { fprintf(stderr,"unknown option: %s\n",argv[i]); return 2; }
    }
    if (split_rows > n-1) split_rows=n-1;
    if (split_rows<0 || shard_count<1 || shard_id<0 || shard_id>=shard_count) return 2;
    N = n*n; started = now(); build_lines();
    int nr=0;
    for (int y=0; y<n; ++y) if (y!=tail) roworder[nr++]=y;
    if (reverse_rows) for (int i=0; i<nr/2; ++i) {
        int t=roworder[i]; roworder[i]=roworder[nr-1-i]; roworder[nr-1-i]=t;
    }
    uint64_t triples=0;
    for (int i=0; i<nl; ++i) {
        unsigned s=(unsigned)pop(line[i]); triples += (uint64_t)s*(s-1)*(s-2)/6;
    }
    fprintf(stderr,"START n=%d lines=%d triples=%"PRIu64" symmetry=%d tail=%d reverse=%d\n",n,nl,triples,symmetry,tail,reverse_rows);
    fflush(stderr);
    search_rows(0,0,0,1,1);
    uint64_t total=0, total_maximal=0;
    for (int k=0;k<=2*n;++k) { add_count(&total,profile[k]); add_count(&total_maximal,maximal[k]); }
    printf("{\"n\":%d,\"total\":%"PRIu64",\"maximal\":%"PRIu64",\"profile\":[",n,total,total_maximal);
    for (int k=0;k<=2*n;++k) printf("%s%"PRIu64,k?",":"",profile[k]);
    printf("],\"maximal_profile\":[");
    for (int k=0;k<=2*n;++k) printf("%s%"PRIu64,k?",":"",maximal[k]);
    printf("],\"seconds\":%.6f,\"prefix_leaves\":%"PRIu64",\"row_nodes\":[",now()-started,prefix_leaves);
    for (int r=0;r<n;++r) printf("%s%"PRIu64,r?",":"",row_nodes[r]);
    printf("],\"freedom_profile\":[");
    for (int k=0;k<=2*n;++k) printf("%s%"PRIu64,k?",":"",freedom_profile[k]);
    printf("],\"program\":\"row\",\"split_rows\":%d,\"shard\":%d,\"shards\":%d,\"frontiers\":%"PRIu64",\"assigned_frontiers\":%"PRIu64",\"cpu_seconds\":%.6f",
           split_rows,shard_id,shard_count,frontier_index,assigned_frontiers,cpu_now());
    printf(",\"lines\":%d,\"triples\":%"PRIu64",\"symmetry\":%d,\"tail\":%d,\"reverse\":%d}\n",nl,triples,symmetry,tail,reverse_rows);
    fflush(stdout);
    fprintf(stderr,"DONE n=%d seconds=%.6f total=%"PRIu64" maximal=%"PRIu64"\n",n,now()-started,total,total_maximal);
    return 0;
}
