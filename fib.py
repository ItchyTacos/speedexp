import time
import sys
sys.set_int_max_str_digits(1000000)

a=0
b=1
n=0
i=0

start = time.perf_counter()
while(True):
    n=a+b
    a=b
    b=n
    i=i+1
    end = time.perf_counter()
    if (end-start > 1):
        break

print(n)
print(i)
print(end-start)