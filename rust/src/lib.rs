use pyo3::prelude::*;
use numpy::PyArray1;

#[pyfunction]
fn compute(n: usize) -> f64 {
    let mut x = 0.0;
    for i in 0..n {
        x += (i % 7) as f64 * 0.1;
    }
    x
}

#[pyfunction]
fn sum_squares(arr: &PyArray1<f64>) -> f64 {
    let slice = unsafe { arr.as_slice().unwrap() };
    slice.iter().map(|x| x * x).sum()
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