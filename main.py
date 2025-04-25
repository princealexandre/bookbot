def get_book_text(filepath):
    with open (filepath) as f: 
        return f.read()
def main():
    book_to_analyze = get_book_text("books/frankenstein.txt")
    print (book_to_analyze)
main ()