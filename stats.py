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
        lower_char = words.lower()
        chars_list = list(lower_char)
        for char in chars_list:
            char_dict[char] += 1

    return char_dict
