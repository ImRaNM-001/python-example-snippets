
# Installation Commands

## Create the Virtual Environment
```bash
python3 -m venv .venv
```

## Activate the Virtual Environment
```bash
source .venv/bin/activate
```

## Test pip Installation
A minimal stub package to test the success of pip install / A stub package for testing if pip install is working.
```bash
pip install pip-install-test
pip uninstall pip-install-test
```

## Upgrade pip
Run the below command in the terminal if the environment path is (inadvertently) changed anywhere in Mac, which causes problems.
```bash
python -m pip install --upgrade pip
```

## Install New Packages 
### (without Upgrading pip)
To install new packages like "pytorch", "sklearn" without upgrading the pip utility, do this:
```bash
    - pip freeze > requirements.txt
    
    - Insert the correct library names "pytorch", "sklearn" WITHOUT the library versions in the aforementioned file then run,
```    

    pip install -r requirements.txt

## Check whether we are inside .venv env or NOT by returning True or False,
```bash
python3 -c "import sys; print(hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix))"
```

## Check any Library Version
Check numpy (or any other lib) version to ensure they are NOT read from outside .venv envs,
```bash
python3 -c "import numpy; print(numpy.__version__)"
```

## Fix mypy Linter Issues
To get rid of the red line after an import in a `.py` file, which is due to mypy linter, do this:
```bash
mypy --install-types
```
### Example Output:
```
mypy.ini: [mypy]: python_version: Invalid python version '3.12.7  # Or your Python version' (expected format: 'x.y')

mypy.ini: [mypy]: strict: Not a boolean: True        # Enables all strict flags

Installing missing stub packages:

/Users/imran-m/python-flask-project/.venv/bin/python3.12 -m pip install types-requests

Install? [yN] Y

Collecting types-requests

Downloading  types_requests-2.32.0.20241016-py3-none-any.whl.metadata (1.9 kB)

Requirement already satisfied: urllib3>=2 in ./.venv/lib/python3.12/site-packages (from types-requests) (2.3.0)

Downloading types_requests-2.32.0.20241016-py3-none-any.whl (15 kB)

Installing collected packages: types-requests

Successfully installed types-requests-2.32.0.20241016
```

## Google C0lab Shortcuts (for data science needs):
1. **Remove vertical line in a code cell**:
    - Open cell Settings on the right side of the cell
    - Go to the "Editor" tab
    - Replace the existing value with '0'

2. **Convert "code" cell to a "text" cell and vice versa**:
    - `CTRL + MM` --> converts to a "text" cell
    - `CTRL + MY` --> converts back to a "code" cell

3. **Check if a package is already installed**:
    ```bash
    !pip list | grep pandas
    ```
    or, for a set of packages:
    ```bash
    !pip list | grep -E 'mlflow|optuna'
    ```
