def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_sorted_list = sort_characters(get_num_characters(text)) 
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    # print(get_num_characters(text))
    print("")
    for item in chars_sorted_list:
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)

def sort_on(dict):
    return dict["num"]


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_characters(text):
    lowered_string = text.lower()
    dictionary = {}
    # dictionary = {chr(i): 0 for i in range(ord('a'), ord('z') +1)}
    for char in lowered_string:
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    return dict(sorted(dictionary.items()))

def sort_characters(dictionary):
    result_list = []
    for entry in dictionary:
        if entry.isalpha():
"""
    This was by and large the only struggle. I converted the dictionary
    into a list of dictionaries, but omitted the keywords... they are free, and so much easier to sort then! OH DEAR! Well, something learned!!!

"""
            result_list.append({"char": entry, "num": dictionary[entry]})
    result_list.sort(reverse=True, key=sort_on)
    return result_list

main()

