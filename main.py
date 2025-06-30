#! /usr/bin/python3

from stats import get_word_count, get_character_count, make_sorted_dict

import sys
import re

def get_book_text(filepath=None):
    if filepath is None:
        return

    lines = []
    with open(filepath, 'r') as book_file:
        lines = book_file.readlines()

    return ''.join(lines)


def pretty_print(book_name, count, sorted_dict):
    center_val = 50
    print(" BOOKBOT ".center(center_val, '='))
    print(f'Analyzing book found at {book_name}...')
    print(" Word Count ".center(center_val, '-'))
    print(f'Found {count} total words')
    print(" Character Count ".center(center_val, '-'))
    for d in sorted_dict:
        k, v = d.values()
        print(f'{k}: {v}')
    print(" END ".center(center_val, '='))


def main():
    books = sys.argv
    
    if len(books) < 2:
        print(f'Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    for book in books[1:]:
        current_book = get_book_text(book)
        word_count = get_word_count(current_book)
        count_dict = get_character_count(current_book)
        sorted_dict = make_sorted_dict(count_dict)
        pretty_print(book, word_count, sorted_dict)

if __name__ == "__main__":
    main()
