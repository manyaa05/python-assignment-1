# Write a program in python that converts a string into a list of its characters 
def string_to_list(input_string):
    return list(input_string)

input_string = input("Enter a string: ")

characters_list = string_to_list(input_string)

print("List of characters:", characters_list)
