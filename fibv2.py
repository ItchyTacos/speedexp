import time

class bignum:
    def __init__(self,mantissa=0.0,exponent=0):
        self.mantissa=mantissa
        self.exponent=exponent
    def __str__(self):
        return f"{self.mantissa}e{self.exponent}"


def bigadd(a: 'bignum', b: 'bignum') -> 'bignum':
    
    a = bignum(a.mantissa,a.exponent)
    b = bignum(b.mantissa,b.exponent)


    while a.exponent > b.exponent:
        b.mantissa /= 10
        b.exponent += 1
    
    while b.exponent > a.exponent:
        a.mantissa /= 10
        a.exponent += 1

    r = bignum(a.mantissa + b.mantissa, a.exponent)

    while r.mantissa >= 10000:
        r.mantissa /= 10
        r.exponent += 1

    while r.mantissa < 1 and r.mantissa != 0:
        r.mantissa *= 10
        r.exponent -= 1

    return r

def main():

    a = bignum(0.0,0)
    b = bignum(1.0,0)
    n = bignum(0.0,0)

    i = 0

    elapsed = 0

    start = time.perf_counter()

    while elapsed < 1:

        n = bigadd(a,b)
        a = b
        b = n

        i += 1

        if ((i % 100) == 0) or (i > 100000):
            end = time.perf_counter()
            elapsed = end - start
    
    print(f"fib[{i}]: {n}")
    print(elapsed)



if __name__ == "__main__":
    main()
