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





