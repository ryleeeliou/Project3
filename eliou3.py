from collections import Counter # Keeps track of count of elements

# Reading and Saving Text in File

def read_text_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        return text
    
def save_text_file(file_path, text):
    with open(file_path, 'w') as file: 
        file.write(text)

# Text Functions

# First, count frequency of ALL words in the text. 
def all_word_count(text):
    words = text.lower().split()
    word_counts = Counter(words)
    common_words = word_counts.most_common(5)
    return common_words

# Function that counts the frequency of ONE word
def single_word_count(text,word):
    word = word.lower().strip()
    if " " in word or not word:
        return "Please enter a single word!"
    word_count = text.lower().split().count(word)
    return word_count

# Function that replaces one word with ANOTHER word 
def replace_word(text, target_word, replacement_word):
    if " " in target_word or " " in replacement_word:
        return "Please enter single words only!"
    target_word = target_word.strip()
    replace_word = replacement_word.strip()
    new_text = text.replace(target_word, replace_word)
    count = text.count(target_word.lower())
    return new_text, count

# Function that adds new text to existing text
def add_text(text, new_text):
    return text + ' ' + new_text #appends 

# Function that deletes first occurence of specific text 
def delete_text(text, text_to_delete):
    index = text.lower().find(text_to_delete.lower())
    if index == -1:
        return text, "Text not found"
    new_text = text[:index] + text[index+len(text_to_delete) : ]
    return new_text

#Function that highlights a specific word in given text
def highlight(text, word):
    highlighted_text = text.replace(word, f'*{word}*') #asterisks around chosen word to highlight it
    return highlighted_text


# Create full menu! (main function...if name == main)

def main():
    file_path = '/Users/ryleeeliou/Desktop/Python/sample.txt'
    text = read_text_file(file_path)

    while True:
        #Display
        print('Edit Menu:')
        print('1: Top 5 most common words')
        print('2: Single Word Frequency')
        print('3: Replace a word')
        print('4: Add Text')
        print('5: Delete Text')
        print('6: Highlight text')
        print('7: Exit')

        user_option = input('Please select an option: ')

        #Menu choices 

        if user_option == '1':
            common_words = all_word_count(text)
            print(common_words)
        
        elif user_option == '2':
            word = input('Please enter word to count: ')
            count = single_word_count(text, word)
            print(f'{word} appears {count} times!')

        elif user_option == '3':
            target_word = input('Please input target word: ')
            replace_word = input('Please input the replacement word: ')
            text, count = replace_word(text, target_word, replace_word)
            print(f'{count} words replaced!')

        elif user_option == '4':
            new_text = input('Please enter the text you would like to add: ')
            text = add_text(text, new_text)

        elif user_option == '5':
            text_to_delete = input('Please enter the text to delete: ')
            text = delete_text(text, text_to_delete)

        elif user_option == '6':
            word = input('Please enter the word to highlight: ')
            text = highlight(text, word)

        elif user_option == '7':
            save_text_file(file_path, text) # saves text in file 
            break #exits loop 

        else:
            print('Invalid choice! Please choose a valid option from the menu.')


if __name__ == "__main__":
    main()
