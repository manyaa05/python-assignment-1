# Write a program in python that counts the frequency of each character in a string
def count_character_frequency(input_string):
    frequency = {}
    
    for char in input_string:
        frequency[char] = frequency.get(char, 0) + 1
    
    return frequency

input_string = input("Enter a string: ")

character_frequency = count_character_frequency(input_string)

print("Character frequency:")
for char, freq in character_frequency.items():
    print(f"'{char}': {freq}")
