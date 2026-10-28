"""text_tools: reusable text helper functions (a custom module)."""


def word_count(text):
    """Count the words in a piece of text.

    Args:
        text (str): The text to count.

    Returns:
        int: The number of words.
    """
    return len(text.split())


def reverse_words(text):
    """Reverse the order of the words in a sentence.

    Args:
        text (str): The sentence.

    Returns:
        str: The same words in reverse order.
    """
    return " ".join(reversed(text.split()))


def is_palindrome(text):
    """Check whether text reads the same forwards and backwards.

    Only letters and digits are compared, and case is ignored.

    Args:
        text (str): The text to check.

    Returns:
        bool: True if the text is a palindrome.
    """
    cleaned = [char.lower() for char in text if char.isalnum()]
    return cleaned == cleaned[::-1]