from stats import count_words, count_chars

def get_book_text(filename):
    with open(filename) as f:
        return f.read()

def main():
    file_contents = get_book_text("books/frankenstein.txt")
    num_words = count_words(file_contents)
    print(f"Found {num_words} total words")
    chars = count_chars(file_contents)
    print(chars)

main()