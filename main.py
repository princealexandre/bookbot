from stats import get_book_text
from stats import get_num_words
from stats import count_characters

text = get_book_text("books/frankenstein.txt")
word_counts = get_num_words(text)
character_counts = count_characters(text)

print (word_counts, character_counts)