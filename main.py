def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    word_length = get_num_words(text)
    print(word_length)
    char_dict = get_chars_dict(text)
    print(char_dict)
    list_chars = dict_list(char_dict)
    print(list_chars)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
        
def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered.isalpha():
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    return chars

def sort_on(dict):
    return dict['num']

def dict_list(dict):
    list_dict = []
    for char in dict:
        num = dict[char]
        char_dict = {'char': char, 'num': num}
        list_dict.append(char_dict)
    list_dict.sort(reverse=True, key=sort_on)
    return list_dict

main()