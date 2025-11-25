import numpy as np
import time

def compute(n):
    x = 0.0
    for i in range(n):
        x += (i % 7) * 0.1
    return x

def sum_squares(a):
    s = 0.0
    for v in a:
        s += v*v
    return s

def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

def bench(fn, *args, repeat=5):
    times = []
    for _ in range(repeat):
        t0 = time.perf_counter()
        fn(*args)
        t1 = time.perf_counter()
        times.append(t1 - t0)
    return min(times)

if __name__ == "__main__":
    N = 500_000
    arr = np.random.rand(N)

    print("compute :", bench(compute, N))
    print("sum_squares :", bench(sum_squares, arr))
    print("fib :", bench(fib, 30))