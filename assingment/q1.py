
# Write a program that takes two numbers as input and prints their sum 
def add_two_numbers():
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    try:
        num1 = float(num1)
        num2 = float(num2)
        sum_result = num1 + num2
        print(f"The sum of {num1} and {num2} is {sum_result}")
    except ValueError:
        print("Please enter valid numbers.")
add_two_numbers()
