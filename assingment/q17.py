# Write a program in python that converts a given string to title case (first letter of each word capitalized)
def convert_to_title_case(input_string):
    return input_string.title()

input_string = input("Enter a string: ")

title_case_string = convert_to_title_case(input_string)

print("String in title case:", title_case_string)
