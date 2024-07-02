def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    print(f"{book_path} has total {word_count} words")


def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()


def get_word_count(text):
    words = text.split()
    return len(words)


main()
