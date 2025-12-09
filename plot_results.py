import subprocess
import re
import matplotlib.pyplot as plt

def run(cmd):
    """Exécute un script Python et retourne sa sortie texte."""
    print(f"Running {cmd}...")
    result = subprocess.run(
        cmd, shell=True, capture_output=True, text=True
    )
    print(result.stdout)
    return result.stdout

# --- Exécution des scripts ---
out_py = run("python python_baseline.py")
out_numba = run("python tests_numba.py")
out_cython = run("python cython_module/test_cython_runner.py")
out_rust = run("python rust/test_rust.py")

PYPY_PATH = r".\pypy3.11\pypy3.exe"
out_pypy = run(f"\"{PYPY_PATH}\" pypy_runner.py")

# --- Extraction automatique des valeurs ---
def extract(out):
    """
    Extrait les trois mesures depuis un texte.
    """
    compute = re.search(r"compute.*?:\s*([\d\.eE+-]+)", out)
    sumsq = re.search(r"sum_squares.*?:\s*([\d\.eE+-]+)", out)
    fib = re.search(r"fib.*?:\s*([\d\.eE+-]+)", out)
    

    return {
        "compute": float(compute.group(1)) if compute else None,
        "sum_squares": float(sumsq.group(1)) if sumsq else None,
        "fib": float(fib.group(1)) if fib else None,
    }

res_python = extract(out_py)
res_numba = extract(out_numba)
res_cython = extract(out_cython)
res_rust = extract(out_rust)
res_pypy = extract(out_pypy)

print("\n--- Résultats détectés ---")
print("Python :", res_python)
print("Numba  :", res_numba)
print("Cython :", res_cython)
print("Rust :", res_rust)
print("PyPy   :", res_pypy)

# --- Vérif ---
if None in res_python.values() or None in res_numba.values() or None in res_cython.values() or None in res_rust.values() or None in res_pypy.values():
    print("\n Certaines valeurs n'ont pas été détectées. Vérifie les sorties.")
    exit()

# --- Graphique ---
labels = ["compute", "sum_squares", "fib"]

plt.figure(figsize=(9, 5))

plt.plot(labels, [res_python[l] for l in labels],
         marker="o", markersize=10, linewidth=2,
         label="Python pur")

plt.plot(labels, [res_numba[l] for l in labels],
         marker="s", markersize=10, linewidth=2,
         label="Numba")

plt.plot(labels, [res_cython[l] for l in labels],
         marker="^", markersize=10, linewidth=2,
         label="Cython")

plt.plot(labels, [res_rust[l] for l in labels],
         marker="d", markersize=10, linewidth=2,
         label="Rust (PyO3)")

plt.plot(labels, [res_pypy[l] for l in labels],
         marker="D", markersize=10,linewidth=2, 
         label="PyPy")


plt.yscale("log") 

plt.xlabel("Fonction testée")
plt.ylabel("Temps d'exécution (s) [échelle log]")
plt.title("Comparaison des performances : Python, Numba, Rust, PyPy et Cython")
plt.legend()
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.tight_layout()
plt.show()
