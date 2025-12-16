# Projet_Prob_Obj

## Installer Python 3.12.x
Necessaire pour la suite et bien verifir qu'il est pris en compte

## Installer Visual Studio Build Tools (COMPILATEUR C)
Installer le minimum :

Desktop development with C++
MSVC v143 (ou +)
Windows 10/11 SDK

Ensuite redémarrer le PC.

## Créer le dossier du projet

mkdir Projet
cd Projet

## Créer l’environnement virtuel

python -m venv venv
.\venv\Scripts\activate

## Installer les dépendances Python
Dans le repertoire venv:

pip install numpy cython numba matplotlib

## Activer l’environnement de compilation C
Ouvrir "Developer Command Prompt for VS2022"

Aller au projet :
cd C:\Users\...\Projet

Activer le venv à l’intérieur de ce terminal :

.\venv\Scripts\activate

## Compiler le module Cython
Aller dans le dossier :

cd cython_module

Lancer la compilation :

python setup.py build_ext --inplace

On devrait obtenir un fichier :

tests_cython.cp312-win_amd64.pyd

## Tester chaque module

Python:
python python_baseline.py

Numba:
python tests_numba.py

Cython:
cd cython_module
python test_cython_runner.py

## Installation et utilisation du module Rust avec Python
Rust (avec cargo):
Installer depuis https://rustup.rs/

Maturin:
pip install maturin

### Compilation et installation du module Rust
Important : faire cela depuis le CMD, pas PowerShell, pour éviter des erreurs d’encodage.

Se placer dans le dossier rust : cd rust

Lancer maturin develop pour compiler et installer le module dans le venv : maturin develop --release

## Tracer le graphique
Retourner a la racine du projet (sortir de cython_module) puis:
python plot_results.py
