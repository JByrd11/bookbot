
from stats import get_num_words

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

def print_report(filename, get_num_words, char_list):
    print(f"--- Begin report of {filename} ---")
    print(f"{get_num_words} words found in the document")  # Changed this line
    print("")
    for i in char_list:
        print(f"The '{i['char']}' character was found {i['count']} times")
    print("")
    print("--- End report ---")

# Main execution
text = get_text_from_file("books/frankenstein.txt")
word_count_result = get_num_words(text)
char_counts = character_count(text)

char_list = []
for char, count in char_counts.items():
    char_dict = {"char": char, "count": count}
    char_list.append(char_dict)

char_list.sort(reverse=True, key=sort_on)
print_report("books/frankenstein.txt", word_count_result, char_list)



def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        
       

if __name__ == "__main__":
    main()



