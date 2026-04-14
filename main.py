import sys
from stats import parse_book_text, num_char_appearances, sorted_dict

print(len(sys.argv))


def get_book_text(file_path):
    with open(file_path, 'r') as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print(f"============ BOOKBOT ============")
    book_text = get_book_text(sys.argv[1])
    print(f"Analyzing book found at {sys.argv[1]}")
    print(f"----------- Word Count ----------")
    parse_book_text(book_text)
    print(f"--------- Character Count -------")
    char_counts = num_char_appearances(book_text)
    print(sorted_dict(char_counts))
    print(f"============= END ===============")


if __name__ == "__main__":
    main()