# Modules and Packages in Python

## What is a module?

A **module** is a single `.py` file containing functions, classes or variables that other code can reuse. Instead of copying code between programs, you write it once in a module and **import** it wherever it's needed.

In this project, `math_tools.py` and `text_tools.py` are custom modules.

## What is a package?

A **package** is a folder of modules, marked by a file named `__init__.py`. Packages let you group related modules together.

```
utilities/
├── __init__.py       # makes this folder a package
├── math_tools.py     # module
└── text_tools.py     # module
```

The `__init__.py` file runs when the package is imported. In this project it re-exports the most useful functions, so users can write `from utilities import is_prime` instead of the longer `from utilities.math_tools import is_prime`.

## Ways to import

| Style | Example | Use it by calling |
|---|---|---|
| Import a module | `import math` | `math.sqrt(16)` |
| Import with an alias | `from utilities import math_tools as mt` | `mt.gcd(48, 18)` |
| Import specific names | `from utilities.text_tools import is_palindrome` | `is_palindrome("level")` |
| Import from a package | `from utilities import factorial` | `factorial(5)` |

Avoid `from module import *`, because it hides where names come from.

## `if __name__ == "__main__":`

Every module has a `__name__`. When a file is run directly, it is `"__main__"`. When it is imported, it is the module's name. Code inside this `if` block runs only when the file is run directly, so a module can include test code without running it on import.

## Three kinds of modules

1. **Standard library:** comes with Python (`math`, `random`, `datetime`, `os`). No installation needed.
2. **Third-party:** written by others and installed with `pip` (`numpy`, `pandas`, `requests`).
3. **Custom:** written by you, like `utilities` in this project.

## Third-party packages and pip

`pip` is Python's package installer:
```
pip install numpy
pip list
pip freeze > requirements.txt
```

A `requirements.txt` file lists the packages a project needs, so anyone can install them with:
```
pip install -r requirements.txt
```

This project uses **NumPy** for fast numerical work on arrays. `third_party_demo.py` shows creating arrays, statistics (`mean`, `median`, `std`), vectorised arithmetic (`marks + 5` with no loop), filtering with a condition, and 2D arrays. It also catches `ImportError`, so a missing package gives a helpful message instead of a crash.

## Why modules and packages matter

- **Reusability:** write once, use in many programs.
- **Organisation:** each file has one clear purpose.
- **Maintainability:** fixing a function in one place fixes it everywhere.
- **Teamwork:** different people can work on different modules.
- **Access to a huge ecosystem** of libraries through `pip`.