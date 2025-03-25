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
def count_char(text):
    char_count = 0
    with open(text) as words:
        chars_lower = words.lower()
        for chars in chars_lower
    return
