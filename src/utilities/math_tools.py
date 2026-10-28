"""math_tools: reusable math helper functions (a custom module)."""


def is_prime(number):
    """Check whether a number is prime.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if number < 2:
        return False
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1
    return True


def factorial(number):
    """Return the factorial of a non-negative integer.

    Args:
        number (int): The number, which must be 0 or more.

    Returns:
        int: number! (for example, factorial(5) is 120).

    Raises:
        ValueError: If the number is negative.
    """
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for value in range(2, number + 1):
        result *= value
    return result


def gcd(first, second):
    """Return the greatest common divisor of two integers.

    Args:
        first (int): The first number.
        second (int): The second number.

    Returns:
        int: The largest number that divides both.
    """
    first, second = abs(first), abs(second)
    while second:
        first, second = second, first % second
    return first


def fibonacci(count):
    """Return the first `count` numbers of the Fibonacci sequence.

    Args:
        count (int): How many numbers to return (0 or more).

    Returns:
        list: The Fibonacci numbers, starting 0, 1, 1, 2, 3, ...

    Raises:
        ValueError: If count is negative.
    """
    if count < 0:
        raise ValueError("Count cannot be negative.")
    sequence = []
    current, following = 0, 1
    for _ in range(count):
        sequence.append(current)
        current, following = following, current + following
    return sequence


if __name__ == "__main__":
    # This block runs only when the file is run directly, not when imported
    print("Testing math_tools directly:")
    print("is_prime(17) =", is_prime(17))
    print("factorial(5) =", factorial(5))