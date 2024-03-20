def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = get_word_count(text)
    letter_counter = get_chars_dict(text)
    sort_dict = create_dictionary(letter_counter)
    sort_dict.sort(reverse=False, key=sort_on)

    print(f"--- Begin report of {book_path} ---")
    print(f"{count} words found in the document.")
    print()
    for item in sort_dict:
        print(f"The {item['char']} character was found {item['count']} times")
    print("--- End report ---")

def create_dictionary(dict):
    char_list = []
    for item in dict:
        char_dict = {}
        if item.isalpha():
            char_dict["char"] = item
            char_dict["count"] = dict[item]
            char_list.append(char_dict)
    return char_list
    
def sort_on(dict):
    return dict["char"]


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_word_count(text):
    words = text.split()
    counter = 0
    for word in words:
        counter += 1
    return counter


# This is the solution from boot.dev
def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars
    

main()