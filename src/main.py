"""Demonstrates importing standard-library modules and a custom package."""

import math
import random
from datetime import date

import utilities                                  # import the whole package
from utilities import math_tools as mt            # import a module with alias
from utilities.text_tools import is_palindrome    # import one function
from utilities import factorial, word_count       # names exported by __init__


def show(title):
    """Print a heading for a section."""
    print(f"\n--- {title} ---")


def main():
    """Run every demonstration."""
    print("Working with Modules and Packages")

    show("1. Standard library modules")
    print("math.sqrt(144) =", math.sqrt(144))
    print("math.pi =", round(math.pi, 4))
    random.seed(7)  # fixed seed so the result is repeatable
    print("random.randint(1, 10) =", random.randint(1, 10))
    print("Today's year (datetime) =", date.today().year)

    show("2. Custom module: utilities.math_tools (imported with an alias)")
    print("mt.is_prime(29) =", mt.is_prime(29))
    print("mt.is_prime(30) =", mt.is_prime(30))
    print("mt.gcd(48, 18) =", mt.gcd(48, 18))
    print("mt.fibonacci(8) =", mt.fibonacci(8))

    show("3. Names imported from the package")
    print("factorial(5) =", factorial(5))
    print("word_count('Modules keep code organised') =",
          word_count("Modules keep code organised"))

    show("4. Custom module: utilities.text_tools")
    print("is_palindrome('A man, a plan, a canal: Panama') =",
          is_palindrome("A man, a plan, a canal: Panama"))
    print("utilities.reverse_words('one two three') =",
          utilities.reverse_words("one two three"))

    show("5. Package information")
    print("Package version:", utilities.__version__)
    print("Exported names:", ", ".join(utilities.__all__))

    show("6. Handling an error raised by a module function")
    try:
        factorial(-3)
    except ValueError as error:
        print("Caught:", error)


if __name__ == "__main__":
    main()