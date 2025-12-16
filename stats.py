# Returns the number of words in file
def get_num_of_words(text):
    num_of_words = 0
    num_of_words = len(text.split())
    return num_of_words

# Returns a dictionary of characters and their frequency in text
def get_num_of_characters(text):
    chars_dict = {}
    for char in text:
        lowercased = char.lower()
        if (lowercased in chars_dict):
            chars_dict[lowercased] += 1
        else:
            chars_dict[lowercased] = 1
    return chars_dict

# Sort a list of dictionaries
def sort_on(items):
    return items["num"]

# dictionary to sorted list
def chars_dict_to_sorted_list(num_char_dict):
    sorted_list = []
    for char, count in num_char_dict.items():
        sorted_list.append({"char": char, "num": count})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list