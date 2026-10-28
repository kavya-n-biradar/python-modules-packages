# Working with Modules and Packages in Python

A beginner Python project for the CodeMore Python Programming Internship (Week 4, Task 1). It shows how to create custom modules and a package, import code in different ways, and use a third-party package (NumPy).

## Project Overview

- `src/utilities/` is a custom **package** containing two **modules**:
  - `math_tools.py`: `is_prime`, `factorial`, `gcd`, `fibonacci`
  - `text_tools.py`: `word_count`, `reverse_words`, `is_palindrome`
- `src/main.py` imports standard-library modules (`math`, `random`, `datetime`) and the custom package using several import styles.
- `src/third_party_demo.py` uses the third-party package **NumPy**.
- `docs/modules_and_packages.md` explains modules, packages, imports and `pip`.

## Project Structure

```
python-modules-packages/
├── README.md
├── .gitignore
├── requirements.txt
├── src/
│   ├── main.py
│   ├── third_party_demo.py
│   └── utilities/
│       ├── __init__.py
│       ├── math_tools.py
│       └── text_tools.py
└── docs/
    ├── modules_and_packages.md
    └── screenshots/
```

## Requirements

- Python 3.8 or newer
- NumPy (listed in `requirements.txt`)

## Setup and How to Run

```bash
git clone https://github.com/kavya-n-biradar/python-modules-packages.git
cd python-modules-packages
pip install -r requirements.txt
python src/main.py
python src/third_party_demo.py
```

If `pip` is not recognised, use `python -m pip install -r requirements.txt`.

## Ways of Importing Used

| Style | Example in `main.py` |
|---|---|
| Import a whole module | `import math` |
| Import the custom package | `import utilities` |
| Import a module with an alias | `from utilities import math_tools as mt` |
| Import one function | `from utilities.text_tools import is_palindrome` |
| Import names exported by `__init__.py` | `from utilities import factorial, word_count` |

## Console Output

### `main.py` (shortened)
```
--- 2. Custom module: utilities.math_tools (imported with an alias) ---
mt.is_prime(29) = True
mt.is_prime(30) = False
mt.gcd(48, 18) = 6
mt.fibonacci(8) = [0, 1, 1, 2, 3, 5, 8, 13]

--- 6. Handling an error raised by a module function ---
Caught: Factorial is not defined for negative numbers.
```

### `third_party_demo.py` (shortened)
```
--- Statistics ---
Mean: 77.71
Median: 78.0
Highest: 95 | Lowest: 58
```

Full screenshots are in [`docs/screenshots/`](docs/screenshots/):
- `pip_install_numpy.png`: installing the third-party package
- `main_output.png`: output of `main.py`
- `third_party_demo_output.png`: output of `third_party_demo.py`

## What I Learned

- How a module is just a `.py` file and a package is a folder with `__init__.py`
- Different ways to import code, and why `from module import *` is avoided
- What `if __name__ == "__main__":` does
- How to install and use a third-party package with `pip`, and why `requirements.txt` matters
- How NumPy arrays make number crunching simpler than loops

## Author

Kavya Biradar