import numpy as np
import time
from rust_impl import compute, sum_squares, fib

def bench(fn, *args, repeat=5):
    times=[]
    for _ in range(repeat):
        t0=time.perf_counter()
        fn(*args)
        t1=time.perf_counter()
        times.append(t1-t0)
    return min(times)



if __name__ == "__main__":
    N = 500_000
    arr = np.load("arr.npy")

    print("compute (rust):", bench(compute, N))
    print("sum_squares (rust):", bench(sum_squares, arr))
    print("fib (rust):", bench(fib, 30))