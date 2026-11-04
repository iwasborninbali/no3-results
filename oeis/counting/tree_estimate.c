/* Knuth random-path estimator of the line_rows.c prefix search tree.
 * This is an ESTIMATE, never an exact enumeration. It reuses the new row
 * constraints so the target is the actual reflection-reduced search tree.
 * A path selects one legal row pattern uniformly at each level. The product
 * of the branching counts is an unbiased estimator of the number of leaves.
 * Standard errors below describe sampling variation, not timing-model error.
 * gcc -O3 -march=native -std=c11 -Wall -Wextra tree_estimate.c -lm -o tree_estimate
 */
#define main unused_exact_main
#include "line_rows.c"
#undef main
#include <math.h>
static uint64_t random_state = UINT64_C(0xc0dedead12345678);
static uint64_t random64(void) {
    uint64_t x=random_state;
    x^=x>>12; x^=x<<25; x^=x>>27;
    random_state=x;return x*UINT64_C(2685821657736338717);
}
static unsigned uniform(unsigned b) {
    uint64_t threshold=(UINT64_C(0)-b)%b,r;
    do { r=random64(); } while(r<threshold);
    return (unsigned)(r%b);
}
static bits hypothetical_cover(int p,bits covered) {
    covered|=bit(p);
    for(int j=0;j<degree[p];++j) {
        int l=incidence[p][j];
        if(occupied[l]==1) covered|=line[l];
    }
    return covered;
}
int main(int argc,char **argv) {
    if(argc<2 || (n=atoi(argv[1]))<2 || n>11) {
        fprintf(stderr,"usage: %s N [samples] [seed]\n",argv[0]);return 2;
    }
    uint64_t samples=argc>2?strtoull(argv[2],0,10):100000;
    if(samples<2) return 2;
    if(argc>3) random_state=strtoull(argv[3],0,10);
    if(!random_state) random_state=1;
    uint64_t seed=random_state;
    N=n*n;tail=n-1;started=now();build_lines();
    long double mean=0,m2=0,total_mean=0,total_m2=0;
    for(uint64_t s=1;s<=samples;++s) {
        memset(occupied,0,sizeof(occupied));
        bits covered=0;int k=0,first_row=1;unsigned weight=1;
        long double product=1;
        for(int y=0;y<n-1;++y) {
            int ps[80],qs[80];unsigned ws[80],bcount=1;
            ps[0]=qs[0]=-1;ws[0]=weight;
            bits a=rowmask[y]&~covered;
            while(a) {
                int p=first(a);a&=a-1;
                unsigned pat=1U<<(p%n),w=pattern_weight(pat,first_row,weight);
                if(w) { ps[bcount]=p;qs[bcount]=-1;ws[bcount++]=w; }
                bits b=a&~hypothetical_cover(p,covered);
                while(b) {
                    int q=first(b);b&=b-1;
                    w=pattern_weight(pat|(1U<<(q%n)),first_row,weight);
                    if(w) { ps[bcount]=p;qs[bcount]=q;ws[bcount++]=w; }
                }
            }
            product*=bcount;
            unsigned j=uniform(bcount);int p=ps[j],q=qs[j];weight=ws[j];
            if(p>=0) { covered=put(p,k++,covered);first_row=0; }
            if(q>=0) covered=put(q,k++,covered);
        }
        long double delta=product-mean;mean+=delta/(long double)s;m2+=delta*(product-mean);
        unsigned m=(unsigned)pop(rowmask[tail]&~covered);
        long double t=product*weight*(1+m+m*(m-1)/2);
        delta=t-total_mean;total_mean+=delta/(long double)s;total_m2+=delta*(t-total_mean);
    }
    printf("{\"n\":%d,\"status\":\"estimate\",\"method\":\"uniform random row-pattern path / Knuth estimator\",\"samples\":%"PRIu64",\"seed\":%"PRIu64",\"prefix_leaves_mean\":%.6Lf,\"prefix_leaves_standard_error\":%.6Lf,\"total_subsets_mean\":%.6Lf,\"total_subsets_standard_error\":%.6Lf,\"seconds\":%.6f}\n",n,samples,seed,mean,sqrtl(m2/(samples-1)/(long double)samples),total_mean,sqrtl(total_m2/(samples-1)/(long double)samples),now()-started);
    return 0;
}
