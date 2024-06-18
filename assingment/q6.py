# Write a program that reads the content of a text file and prints it to the console
def read_and_print_file():
    filename = "output.txt"
    
    try:
        with open(filename, 'r') as file:
            content = file.read()
            
            print("File content:")
            print(content)
    except FileNotFoundError:
         print(f"The file {filename} does not exist.")
    except IOError:
        print(f"An error occurred while reading the file {filename}.")

read_and_print_file()
