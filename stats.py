def get_num_words(text):
    try:
        words = text.split()  # Split the text into words based on whitespace
        return len(words)     # Return the number of words
    except Exception as e:
        print(f"Could not get number of words from the book: {e}")
        return 0


def get_num_chars(text): 
    text = text.lower() 
    char_dict = {}
    
    for char in text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
        
    
    return char_dict

def sort_on(item):
    return item["num"]


def sort_characters(char_dict):
    char_list = [
        {"char": char, "num": count}
        for char, count in char_dict.items()
        if char.isalpha()
    ]

    char_list.sort(reverse=True, key=sort_on)
    return char_list