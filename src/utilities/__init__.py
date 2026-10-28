"""utilities: a small package of reusable math and text helpers.

Importing the package gives direct access to the most-used functions:

    from utilities import is_prime, word_count
"""

from .math_tools import factorial, fibonacci, gcd, is_prime
from .text_tools import is_palindrome, reverse_words, word_count

__all__ = [
    "factorial",
    "fibonacci",
    "gcd",
    "is_prime",
    "is_palindrome",
    "reverse_words",
    "word_count",
]
__version__ = "1.0"