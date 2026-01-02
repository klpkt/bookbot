import sys
from stats import count_words, count_chars, sort_counts

def get_book_text(filename):
    with open(filename) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filename = sys.argv[1]

    file_contents = get_book_text(filename)
    num_words = count_words(file_contents)
    chars = count_chars(file_contents)
    sorted_chars = sort_counts(chars)

    print( "============ BOOKBOT ============")
    print(f"Analyzing  book found at {filename}")
    print( "----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print( "--------- Character Count -------")
    for item in sorted_chars:
        if not item["char"].isalpha(): continue
        print(f"{item["char"]}: {item["num"]}")

main()