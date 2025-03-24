def main():
    book_path = "books/frankenstein.txt"
    print_text = get_book_text(book_path)
    count_words = count_book_text(book_path)

    print(f"{count_words} words found in the document")

# Gets the file path as input and returns contents of a file as a string
def get_book_text(b):
    with open(b) as book:
        return book.read()

#Counts number of words in the input string
def count_book_text(text):
    word_count = 0
    with open(text) as words:
        string = words.read()
        word_list  = string.split()

        for w in word_list:
            word_count += 1
    return word_count

main()
