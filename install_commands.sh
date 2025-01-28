#!/usr/bin/env bash

# create the virtual env
python3 -m venv .venv

# activate the virtual env
source .venv/bin/activate


# A minimal stub package to test success of pip install / A stub package for testing if pip install is working.
pip install pip-install-test
pip uninstall pip-install-test

# run below command in termnial if foolishly changed environment path anywhere in Mac which causes problems
python -m pip install --upgrade pip



""" to install new packages like "pytorch", "sklearn" without upgrading the pip utility, do this:
    --> pip freeze > requirements.txt 
    --> insert the correct lib names "pytorch", "sklearn" WITHOUT the library versions in the aforementioned file, then run
"""
pip install -r requirements.txt



# checks whether we are inside .venv env or NOT by returning True or False
python3 -c "import sys; print(hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix))"


# check numpy (or any other lib) version to ensure they are NOT read from outside .venv envs
python3 -c "import numpy; print(numpy.__version__)"



""" to get rid of red line after an import in a .py file, which is due to mypy linter, do this:
    --> mypy --install-types 
    --> OUTPUT:
            mypy.ini: [mypy]: python_version: Invalid python version '3.12.7  # Or your Python version' (expected format: 'x.y')
            mypy.ini: [mypy]: strict: Not a boolean: True        # Enables all strict flags
            Installing missing stub packages:
            /Users/imran-m/python-flask-project/.venv/bin/python3.12 -m pip install types-requests

            Install? [yN] Y

            Collecting types-requests
            Downloading types_requests-2.32.0.20241016-py3-none-any.whl.metadata (1.9 kB)
            Requirement already satisfied: urllib3>=2 in ./.venv/lib/python3.12/site-packages (from types-requests) (2.3.0)
            Downloading types_requests-2.32.0.20241016-py3-none-any.whl (15 kB)
            Installing collected packages: types-requests
            Successfully installed types-requests-2.32.0.20241016

"""

"""
Google C0lab shortuts:
------------
1> Remove vertical line in a code cell,
Open cell Settings on right side of cell >> "Editor" tab >> Replace existing value with '0'


2> convert "code" cell to a "text" cell and vice versa,
CTRL + MM --> converts to a "text" cell
CTRL + MY --> converts back to a "code" cell


3> check if a package is already installed,
!pip list | grep pandas 

or, for a set of packages,
!pip list | grep -E 'mlflow|optuna'






"""













