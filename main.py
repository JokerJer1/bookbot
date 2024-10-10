def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)

    characters = count_characters(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    sorted_chars = count_characters(text)
    for char, count in sorted_chars:
        print(f"{char}: {count}")
    print("--- End report ---")



def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_characters(text):
    characters = {}
    for char in text.lower():
        if char.isalpha():
            characters[char] = characters.get(char, 0) + 1
    return sorted(characters.items(), key=lambda x: x[1], reverse=True)

    
    

main()