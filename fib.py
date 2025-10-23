import time

a=0
b=1
n=0
i=0
elapsed = 0

start = time.perf_counter()
while(elapsed <= 1):
    n=a+b
    a=b
    b=n
    i=i+1
    end = time.perf_counter()
    elapsed = end - start

print(f"fib[{i}]")
print(end-start)
