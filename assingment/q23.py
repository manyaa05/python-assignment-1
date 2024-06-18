# Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

temperature = float(input("Enter the temperature value: "))
unit = input("Enter the temperature unit (C for Celsius, F for Fahrenheit): ")

if unit.upper() == 'C':
    fahrenheit = celsius_to_fahrenheit(temperature)
    print(f"{temperature}°C is equal to {fahrenheit:.2f}°F.")
elif unit.upper() == 'F':
    celsius = fahrenheit_to_celsius(temperature)
    print(f"{temperature}°F is equal to {celsius:.2f}°C.")
else:
    print("Invalid temperature unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
