# Write a python program that calculates the sum of the digits of a given number
def sum_of_digits(number):
    digit_sum = 0
    
    number_str = str(number)
    
    for digit in number_str:
        digit_sum += int(digit)
    
    return digit_sum

number = int(input("Enter a number: "))

result = sum_of_digits(number)

print(f"The sum of the digits of {number} is: {result}")
