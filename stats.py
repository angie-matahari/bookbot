def get_word_count(text: str) -> int:
    """Counts the number of words in a given text.

    Args:
        text (str): The input text.
    Returns:
        int: The number of words in the text.
    """
    words = text.split()
    return len(words)
