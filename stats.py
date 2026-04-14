def parse_book_text(book_text):
    # This function will parse the book text and return a count of words.
    words = book_text.split()
    print(f"Found {len(words)} total words")

def num_char_appearances(book_text):
    # This function will count the appearances of each character in the book text.
    char_count = {}
    for char in book_text.lower():
        if char.isalpha():      #.isalpha() specifically selects ONLY the alphanumeric characters
            char_count[char] = char_count.get(char, 0) + 1
    return char_count
    
def sorted_dict(table):
    #This function will sort a dictionary by its values and return the sorted items.
    sort_list = list(table.items())
    sort_list.sort(key=lambda kv: kv[1], reverse=True)

    #Print the dictionary items in their own individual rows
    for key, value in sort_list:
        print(f"{key}: {value}")
    


    