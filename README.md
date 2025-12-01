# Projet_Prob_Obj

## Installer Python 3.12.x

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

## Arborescence général du projet
Projet/
 ├── venv/
 ├── python_baseline.py
 ├── tests_numba.py
 ├── plot_results.py
 ├── cython_module/
 │     ├── __init__.py
 │     ├── tests_cython.pyx
 │     ├── setup.py
 │     ├── test_cython_runner.py
 └── rust/

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

## Tracer le graphique
Retourner a la racine du projet (sortir de cython_module) puis:
python plot_results.py
