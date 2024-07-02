def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_count = get_chars_count(text)
    arr_dict = convert_dict_to_array_dict(char_count)
    sort_array_dict(arr_dict)
    print_report(book_path, word_count, arr_dict)


def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()


def get_word_count(text):
    words = text.split()
    return len(words)


def get_chars_count(text):
    lower_text = text.lower()
    char_count = {}
    for c in lower_text:
        if c not in char_count:
            char_count[c] = 0
        char_count[c] += 1
    return char_count


def convert_dict_to_array_dict(dict):
    array = []
    for k in dict:
        if k.isalpha():
            array.append({
                "char": k,
                "count": dict[k]
            })
    return array


def sort_on(dict):
    return dict["count"]


def sort_array_dict(dict):
    dict.sort(reverse=True, key=sort_on)


def print_report(book_path, word_count, char_count):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()
    for d in char_count:
        print(f"The '{d["char"]}' character was found {d["count"]} times")
    print("--- End report ---")


main()
