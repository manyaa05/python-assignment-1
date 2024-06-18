#Write a python program that checks whether a given number is even or odd
def check_even_or_odd():
    num = input("Enter a number: ")
    
    try:
        num = int(num)
        
        if num % 2 == 0:
            print(f"{num} is even.")
        else:
            print(f"{num} is odd.")
    except ValueError:
        print("Please enter a valid integer.")

check_even_or_odd()
