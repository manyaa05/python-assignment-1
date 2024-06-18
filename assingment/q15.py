# Write a program that reads data from a CSV file and prints it to the console
import csv

def read_and_print_csv(filename):
    try:
        with open(filename, 'r') as file:
            # Create a CSV reader object
            reader = csv.reader(file)
            
            # Read and print each row in the CSV file
            for row in reader:
                print(row)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

csv_file = "data.csv"

read_and_print_csv(csv_file)
