# Gets the file path as input and returns contents of a file as a string
def get_book_text(b):
    with open(b) as book:
        return book.read()

def main():
    print(get_book_text("books/frankenstein.txt"))

main()
