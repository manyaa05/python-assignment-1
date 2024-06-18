# Write a python program that takes a list of numbers and returns their sum
def calculate_sum(numbers):
    return sum(numbers)

numbers = input("Enter a list of numbers separated by spaces: ").split()

numbers = [int(num) for num in numbers]

total_sum = calculate_sum(numbers)

print("Sum of the numbers:", total_sum)