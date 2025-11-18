from stats import get_word_count


def get_book_text(file_path: str):
    """Reads the content of a book from a text file.

    Args:
        file_path (str): The path to the text file containing the book.
    Returns:
        str: The content of the book as a string.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def main():
    book_path = 'books/frankenstein.txt'
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    print(f"Found {word_count} total words.")


main()
