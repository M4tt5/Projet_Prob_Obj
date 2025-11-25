# cython: boundscheck=False, wraparound=False
import numpy as np
cimport numpy as np

cpdef double compute(int n):
    cdef double x = 0.0
    cdef int i
    for i in range(n):
        x += (i % 7) * 0.1
    return x

cpdef double sum_squares(np.ndarray[np.float64_t, ndim=1] a):
    cdef double s = 0.0
    cdef Py_ssize_t i, n = a.shape[0]
    for i in range(n):
        s += a[i] * a[i]
    return s

cpdef int fib(int n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
