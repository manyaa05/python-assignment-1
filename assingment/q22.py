# Write a python program that returns the minimum and maximum values in a list of numbers
def find_min_max(input_list):
    if len(input_list) == 0:
        return None, None
    else:
        return min(input_list), max(input_list)

input_list = input("Enter a list of numbers separated by spaces: ").split()

input_list = [int(num) for num in input_list]

minimum_value, maximum_value = find_min_max(input_list)

if minimum_value is None:
    print("The list is empty.")
else:
    print("Minimum value:", minimum_value)
    print("Maximum value:", maximum_value)
