# Write a python program that counts the occurrences of a specific element in a list
def count_occurrences(input_list, element):
    return input_list.count(element)

input_list = input("Enter a list of numbers separated by spaces: ").split()

input_list = [int(num) for num in input_list]

element = int(input("Enter the element to count occurrences for: "))

occurrences = count_occurrences(input_list, element)

print(f"The element {element} occurs {occurrences} time(s) in the list.")
