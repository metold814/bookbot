def count_char(text):
    char_count = {} # init empty dict
    text = text.lower() # convert to lowercase
    
    for char in text: # for each char in text
        if char.isalpha(): # only alphabets
            if char in char_count: # if char exists in the dic
                char_count[char] += 1 # add 1 to the value
            else: 
                char_count[char] = 1  # else keep the value the same 
    return char_count 
            
def count_words(text):
    # "returns the number of words in a given text"
    words = text.split()
    return len(words)
def print_report(word_count, char_count):
    """Prints a nicely formatted report with word and character counts"""
    print("\n--- Begin report of books/frankenstein.text ---")
    # sort the dictionary by character frequency in descending order

    sorted_char_count = sorted(char_count.items(), key=lambda x: x[1], reverse=True)

    for char, count in sorted_char_count:
        print(f"The '{char}' character was found {count} times")

    print("--- End report ---")



def main():
    # open file and read its contents
    with open("books/frankenstein.txt", "r") as f:   
        file_contents = f.read()

    # Count words and characters
    word_count = count_words(file_contents)
    char_count = count_char(file_contents)   
    # Print the report 
    print_report(word_count, char_count)     


# check if the script is being run directly
if __name__=="__main__":
    main()

