import numpy as np

N = 500_000
rng = np.random.default_rng(seed=12345)
arr = rng.random(N)

np.save("arr.npy", arr)     # format natif NumPy