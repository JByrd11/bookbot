from stats import get_num_words
import sys

def get_text_from_file(path):
    with open(path) as f:
        return f.read()

def character_count(string):
    lowered = string.lower()
    char_counts = {}
    for char in lowered:
        if char.isalpha():
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
    return char_counts

def sort_on(dict):
    return dict["count"]

def print_report(filename, word_count, char_list):
    print(f"--- Begin report of {filename} ---")
    print(f"{word_count} words found in the document")
    print("")
    for i in char_list:
        print(f"The '{i['char']}' character was found {i['count']} times")
    print("")
    print("--- End report ---")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path_to_book = sys.argv[1]
    
    text = get_text_from_file(path_to_book)
    word_count_result = get_num_words(text)
    char_counts = character_count(text)
    
    char_list = []
    for char, count in char_counts.items():
        char_dict = {"char": char, "count": count}
        char_list.append(char_dict)
    
    char_list.sort(reverse=True, key=sort_on)
    print_report(path_to_book, word_count_result, char_list)

if __name__ == "__main__":
    main()