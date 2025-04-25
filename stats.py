def get_book_text(filepath):
     with open (filepath) as f: 
        return f.read()
def get_num_words(text):
        words = text.split()
        num_words = len(words)
        return (num_words)
text = get_book_text("books/frankenstein.txt")
num_words = get_num_words(text)
print(f"{num_words} words found in the document")