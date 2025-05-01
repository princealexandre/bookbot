from stats import get_book_text, get_num_words, count_characters, turn_dictionary_into_sorted_list

def main():
    filepath = "books/frankenstein.txt"
    text = get_book_text(filepath)
    word_counts = get_num_words(text)
    character_counts = count_characters(text)
    sorted_characters = turn_dictionary_into_sorted_list (character_counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_counts} total words")
    print("--------- Character Count -------")  
    for char_dict in sorted_characters:
        char = char_dict["char"]
        count = char_dict["num"]
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

if __name__ == "__main__":
    main()