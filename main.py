import sys
from stats import get_num_words, get_num_character, sorted_list_dict

def get_book_text(file_path):
    """return the text of the file"""
    with open(file_path, "r") as f:
        text = f.read()
        return text

def main():
    if not len(sys.argv) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    my_text = get_book_text(sys.argv[1])
    num_words = get_num_words(my_text)
    num_char = get_num_character(my_text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    my_sorted_dict = sorted_list_dict(num_char)
    for element in my_sorted_dict:
        print(f"{element['char']}: {element['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()
