from stats import count_book_text, count_book_char, sort_book_char
import sys

def main():
    if len(sys.argv) > 1:    
        book_path = sys.argv[1]
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

    else:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
# Gets the file path as input and returns contents of a file as a string
#def get_book_text(b):
#    with open(b) as book:
#        return book.read()

main()
