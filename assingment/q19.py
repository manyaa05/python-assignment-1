# Write a python program that removes all punctuation from a given string
def remove_punctuation(input_string):
    punctuation_chars = string.punctuation
    
    translation_table = str.maketrans('', '', punctuation_chars)
    
    cleaned_string = input_string.translate(translation_table)
    
    return cleaned_string
    
input_string = input("Enter a string with punctuation: ")

cleaned_string = remove_punctuation(input_string)

print("String without punctuation:", cleaned_string)