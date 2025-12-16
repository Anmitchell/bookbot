import sys
from stats import (
    get_num_of_words, 
    get_num_of_characters, 
    chars_dict_to_sorted_list
    )

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_of_words = get_num_of_words(text)
    chars_dict = get_num_of_characters(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print_report(book_path, num_of_words, chars_sorted_list)

# Return text in book
def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
        return file_contents

def print_report(book_path, num_of_words, chars_sorted_list):
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}")
        print("----------- Word Count ----------")
        print(f"Found {num_of_words} total words")
        print("--------- Character Count -------")
        for item in chars_sorted_list:
            print(f"{item["char"]}: {item["num"]}")

        print("============= END ===============")

main()

