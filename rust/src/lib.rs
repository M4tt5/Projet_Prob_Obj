use pyo3::prelude::*;
use ndarray::Array1;
use ndarray_npy::read_npy;

#[pyfunction]
fn compute(n: usize) -> f64 {
    let mut x = 0.0;
    for i in 0..n {
        x += (i % 7) as f64 * 0.1;
    }
    x
}

#[pyfunction]
fn sum_squares(path: String) -> PyResult<f64> {
    // Charge directement arr.npy
    let arr: Array1<f64> = read_npy(path).unwrap();

    let mut s = 0.0;
    for v in arr.iter() {
        s += v * v;
    }
    Ok(s)
}

fn fib_rec(n: i32) -> i32 {
    if n < 2 {
        return n;
    }
    fib_rec(n - 1) + fib_rec(n - 2)
}

#[pyfunction]
fn fib(n: i32) -> i32 {
    fib_rec(n)
}

#[pymodule]
fn rust_impl(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(compute, m)?)?;
    m.add_function(wrap_pyfunction!(sum_squares, m)?)?;
    m.add_function(wrap_pyfunction!(fib, m)?)?;
    Ok(())
}
