def main():
    # Prints the contents of the book to console
    print(get_book_text("books/frankenstein.txt"))

# Gets the file path as input and returns contents of a file as a string
def get_book_text(b):
    with open(b) as book:
        return book.read()



main()
