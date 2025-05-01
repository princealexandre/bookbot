def get_book_text(filepath):
     with open (filepath) as f: 
        return f.read()
def get_num_words(text):
        words = text.split()
        num_words = len(words)
        return (num_words)

def count_characters (text):
     numbers_dictionary = {}
     lowercase_text = text.lower()
     for letter in lowercase_text:
        if letter in numbers_dictionary:
          numbers_dictionary[letter] = numbers_dictionary[letter] + 1
        else: numbers_dictionary[letter] = 1
     return numbers_dictionary   

def turn_dictionary_into_sorted_list(char_dict):
    chars_list = []
    for char, count in char_dict.items():
        chars_list.append({"char": char, "num": count})
    def sort_on(dict):
        return dict["num"]
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list