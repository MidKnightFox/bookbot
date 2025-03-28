from stats import count_book_text
from stats import count_book_char
from stats import sort_book_char

def main():
    book_path = "books/frankenstein.txt"
    #print_text = get_book_text(book_path)
    count_words = count_book_text(book_path) # count number of words in the input text
    count_char = count_book_char(book_path) # count number of characters in the input text
    sorted_char_count = sort_book_char(count_char) # Generate report
    
    #Print results/report
    print(f'''============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------
Found {count_words} total words
--------- Character Count -------''')
    for char_data in sorted_char_count:
        if char_data["char"].isalpha():
            print(f"{char_data['char']}: {char_data['count']} ")
    print("============= END ===============")
    


# Gets the file path as input and returns contents of a file as a string
#def get_book_text(b):
#    with open(b) as book:
#        return book.read()

main()
