# common_words.py

def dynamic_word_counter(filenames):
    """This function asks the user for an input of the word they want to count 
        and counts that word."""
    try:
        print("This program reads files and determines how times a word is used.")   
        word_to_count = input("Please input the word you would like to count in "\
            "the specified texts: ")
        for filename in filenames:
            with open(filename, encoding='utf-8') as file_object:
                content = file_object.read()
                word_count = content.lower().count(word_to_count)
            print(f"{filename} contains {word_count:,} instances of the word "\
                f"'{word_to_count}.'")
    except FileNotFoundError:
        pass


filenames = ['the_great_gatsby.txt','siddhartha.txt','moby_dick.txt','emma.txt']
dynamic_word_counter(filenames)