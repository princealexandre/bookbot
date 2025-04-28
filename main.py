from stats import get_book_text, get_num_words, count_characters, turn_dictionary_into_sorted_list

def main():
    filepath = "books/frankenstein.txt"
    text = get_book_text(filepath)
    word_counts = get_num_words(text)
    character_counts = count_characters(text)
    sorted_characters = turn_dictionary_into_sorted_list (character_counts)

    print (word_counts, character_counts)