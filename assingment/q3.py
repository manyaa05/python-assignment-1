# Write a python program that calculates the factorial of a given number.
def calculate_factorial():
    num = input("Enter a number: ")
    
    try:
        num = int(num)
        
        if num < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            factorial = 1
            for i in range(1, num + 1):
                factorial *= i
            print(f"The factorial of {num} is {factorial}")
    except ValueError:
        print("Please enter a valid integer.")

calculate_factorial()
