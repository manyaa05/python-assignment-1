# Write a program that asks the user for their birth year and calculates their age
def calculate_age(birth_year):
    current_year = 2024  # You can replace this with datetime.datetime.now().year for dynamic current year
    
    age = current_year - birth_year
    
    return age

birth_year = int(input("Enter your birth year: "))

age = calculate_age(birth_year)

print(f"You are {age} years old.")
