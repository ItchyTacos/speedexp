#include <stdio.h>
#include <time.h>

typedef struct
{
    double m;
    long long e;
} bignum;

bignum bigadd(bignum a, bignum b){

    while (a.e > b.e){
        b.m /= 10.0;
        b.e++;
    }

    while (b.e > a.e){
        a.m /= 10.0;
        a.e++;
    }

    bignum r;
    r.m = a.m+b.m;
    r.e = a.e;

    while (r.m >= 10000.0){
        r.m /= 10.0;
        r.e++;
    }
    while (r.m < 1.0 && r.m != 0.0){
        r.m *= 10.0;
        r.e--;
    }
    return r;
}




int main(void){

    bignum a = {0.0,0};
    bignum b = {1.0,0};
    bignum n = {0.0,0};

    double elapsed = 0;

    int i = 0;

    clock_t start = clock();

    while (elapsed < 1.0){

        n = bigadd(a,b);
        a = b;
        b = n;

        i++;

        if ((i % 30000) == 0){
            clock_t end = clock();
            elapsed = (double)(end - start) / CLOCKS_PER_SEC;
        }
    }

    printf("fib[%d]: %.8lfe%lld\n",i-1,n.m,n.e);
    printf("Time elapsed: %.4f\n", elapsed);

    return 0;
}
