from stats import count_book_text

def main():
    book_path = "books/frankenstein.txt"
    #print_text = get_book_text(book_path)
    count_words = count_book_text(book_path)
    count_char = count_book_char(book_path)

    print(f"{count_words} words found in the document")
    print(count_char)


# Gets the file path as input and returns contents of a file as a string
#def get_book_text(b):
#    with open(b) as book:
#        return book.read()

main()
