# Write a python program that checks if two strings are anagrams of each other
def are_anagrams(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()
    
    sorted_string1 = sorted(string1)
    sorted_string2 = sorted(string2)
    
    return sorted_string1 == sorted_string2

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if are_anagrams(string1, string2):
    print("The two strings are anagrams.")
else:
    print("The two strings are not anagrams.")
