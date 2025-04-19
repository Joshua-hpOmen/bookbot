import sys
from stats import count_chars
from stats import count_words
try:
    sys.argv[1]
except:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
def get_book_text(file_path):
    with open(file_path) as f:
        file_input = f.read()
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(f"Found {count_words(file_input)} total words")
        print("--------- Character Count -------")
        count_chars(file_input)
        print("============= END ===============")

get_book_text(sys.argv[1])

