from data_structures.hashtable import Hashtable
import re

def first_repeated_word(input_string):
    collection = Hashtable()
    removed_punctuation = remove_punctuation(input_string)
    parsed_input = removed_punctuation.split()

    for word in parsed_input:
        word = word.lower()
        if collection.has(word):
            return word
        collection.set(word, True)

    return None


def remove_punctuation(input_string):
    pattern = r'[^\w\s]'
    filtered = re.sub(pattern, '', input_string)
    return filtered
