# Write a program that copies the contents of one text file to another
def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source, open(destination_file, 'w') as destination:
            destination.write(source.read())
        print("Contents copied successfully from", source_file, "to", destination_file)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)

source_file = input("Enter the path of the source file: ")
destination_file = input("Enter the path of the destination file: ")

copy_file(source_file, destination_file)
