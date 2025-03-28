#Counts number of words in the input string
def count_book_text(text):
    word_count = 0
    with open(text) as words:
        string = words.read()
        word_list  = string.split()

        for w in word_list:
            word_count += 1
    return word_count

# Count number of characters (in progress)
def count_book_char(text):
    char_count = 0
    char_dict = {}
    with open(text) as words:
        string = words.read()
        chars_list = list(string.lower())
        for char in chars_list:
            if char in char_dict:
                char_dict[char] += 1
            else:
                 char_dict[char] = 1

    return char_dict

# Sort characters by number of times it appears
def sort_book_char(dict):
    # Transform the dictionary into a list of dictionaries
    list = []
    for char, count in dict.items():
        if char.isalpha():# Only include alphabetical characters
            list.append({"char": char, "count":count})
    
    # Sort the list by count (highest to lowest)
    list.sort(reverse=True, key=lambda x: x["count"])

    return list