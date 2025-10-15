
import sys
from stats import get_num_words ,get_num_chars , sort_characters

def get_book_text(path_to_file):
    try:
        with open(path_to_file) as f:
            return f.read()
    except Exception as e:
        print(f"There was an issue getting the book: {e}") 
        return None


def main():
    if len(sys.argv) !=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    
    path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    
    text = get_book_text(path)
    if text is None:
        sys.exit(1)
        
    num_words = get_num_words(text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    char_count = get_num_chars(text)
    sorted_chars = sort_characters(char_count)

    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")



# Entry point of the program
main()
