/* greedy_budget.c — the fixed-budget greedy measurement of Section 7 (A280537 note, v4.3), shipped for reproducibility.
   One seed, one core, a fixed wall-clock budget: uniform random greedy restarts in the n-cube. A restart starts from the empty
   set and repeatedly draws a cell uniformly among the ALIVE cells (cells that can be added without creating a collinear
   triple or a coplanar quadruple), adds it and kills the cells it invalidates, until no cell is alive. Records the number
   of restarts and the best size; a seed "reaches" the target when best >= target.
   usage: ./greedy_budget n seconds seed target        (prints one line: n seed seconds restarts best reached) */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
static int n, N; static int X[4096], Y[4096], Z[4096];
static unsigned long long rng; static unsigned long long xr(void){ rng ^= rng << 13; rng ^= rng >> 7; rng ^= rng << 17; return rng; }
static double now(void){ struct timespec t; clock_gettime(CLOCK_MONOTONIC, &t); return t.tv_sec + t.tv_nsec * 1e-9; }
static int coplanar(int a, int b, int c, int d){ long ux=X[b]-X[a],uy=Y[b]-Y[a],uz=Z[b]-Z[a],vx=X[c]-X[a],vy=Y[c]-Y[a],vz=Z[c]-Z[a],wx=X[d]-X[a],wy=Y[d]-Y[a],wz=Z[d]-Z[a];
  return ux*(vy*wz-vz*wy)-uy*(vx*wz-vz*wx)+uz*(vx*wy-vy*wx)==0; }
static int collinear(int a, int b, int c){ long ux=X[b]-X[a],uy=Y[b]-Y[a],uz=Z[b]-Z[a],vx=X[c]-X[a],vy=Y[c]-Y[a],vz=Z[c]-Z[a];
  return uy*vz==uz*vy && uz*vx==ux*vz && ux*vy==uy*vx; }
int main(int argc, char**argv){ n=atoi(argv[1]); double budget=atof(argv[2]); unsigned long long seed=strtoull(argv[3],0,10); int target=atoi(argv[4]);
  N=n*n*n; int k=0; for(int x=0;x<n;x++)for(int y=0;y<n;y++)for(int z=0;z<n;z++){X[k]=x;Y[k]=y;Z[k]=z;k++;}
  rng = seed * 0x9E3779B97F4A7C15ULL + 0x2545F4914F6CDD1DULL; if(!rng) rng=1;
  static char alive[4096]; static int aliveList[4096]; int S[64]; long restarts=0; int best=0; double t0=now();
  while(now()-t0 < budget){
    memset(alive,1,N); int m=0;
    for(;;){ int na=0; for(int i=0;i<N;i++) if(alive[i]) aliveList[na++]=i; if(!na) break;
      int p=aliveList[xr()%na]; /* kill cells invalidated by p */
      for(int i=0;i<N;i++){ if(!alive[i]||i==p) continue; int dead=0;
        for(int a=0;a<m&&!dead;a++){ if(collinear(S[a],p,i)) dead=1; else for(int b=a+1;b<m&&!dead;b++) if(coplanar(S[a],S[b],p,i)) dead=1; }
        if(dead) alive[i]=0; }
      alive[p]=0; S[m++]=p; }
    restarts++; if(m>best) best=m; }
  printf("n=%d seed=%llu seconds=%.1f restarts=%ld best=%d target=%d reached=%s\n", n, seed, budget, restarts, best, target, best>=target?"yes":"no"); return 0; }
