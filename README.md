# Speed Experiment

In order to chase the biggest number possible, one must consider every possibility.  
This project explores how different programming languages, operating systems, and hardware overheads affect the speed of my Fibonacci program.

---

## Disclaimer

I got this idea from the thumbnail and title of a YouTube video. However, I didn’t actually watch it.  
Video link: [https://youtu.be/KzT9I1d-LlQ?si=k5_0YiSJ0cxB0RCU](https://youtu.be/KzT9I1d-LlQ?si=k5_0YiSJ0cxB0RCU)

---

## Discussion and Results

### `fib.py` — The Baseline

The first program, **fib.py**, was written in Python. the simplest and slowest by design.  
Ease of use is Python’s greatest strength, but also its main bottleneck in raw speed.  
This served as my **baseline**, since Python is the language I’m most comfortable with.

It calculated Fibonacci numbers with great precision, thanks to Python’s dynamic memory allocation for integers. The values easily surpassed the 64-bit unsigned integer limit, but I ran into an issue when printing numbers larger than Python’s integer-to-string conversion limit (defaulted to **4300 digits**).  

Originally, I planned to remove or raise this limit, but decided against it since it could cause problems later in testing consistency.

---

### `fib.c` — The First Optimization

The next program, **fib.c**, was my first major step forward.  
Very unfamiliar with C, GCC, or even how VSCode handles C projects, this was definitely an exercise in learning new syntax, data structures, and stricter conventions than I was used to.

I knew C translated closely to x86 assembly, and I wanted to exploit that to get the most speed possible.  
However, as I predicted while working on `fib.py`, the **64-bit limit** of the `long long` data type was a serious issue, just as I predicted. Even in `printf()`, overflow errors completely broke the output.

To fix this, I changed my approach and implemented a **custom scientific number structure**, one that could represent much larger values without overflowing.  
This allowed me to trade a bit of precision for stability and control. And, most importantly, a consistent number.

---

### `fibv2.c` — Timing Optimization

`fibv2.c` introduced a timing optimization.  
I realized I could take advantage of the CPU’s ability to perform thousands of calculations per microsecond and **only call the hardware timer when the iteration counter was divisible by 10,000**.  

Those extra calculations after each time sample don’t show up in the timing precision, and thus are fair game.  
This change massively improved performance and consistency, as shown in the data.

---

### `fibv2.py` — Translating Improvements

Finally, **fibv2.py** brought those same optimizations back into Python.  
It reduced the precision and only checked time every 10,000 iterations, similar to the C version.  
The purpose was to provide a new **Python baseline** for comparison — and to practice translating algorithms between Python and C while maintaining functional parity.

---

## Results

*Results and timing data will be added once all benchmarks are complete.*


