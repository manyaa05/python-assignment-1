# Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines
def read_multiple_lines():
    lines = []
    while True:
        line = input("Enter a line (or press Enter to finish): ")
        if line:
            lines.append(line)
        else:
            break
    return lines

def print_lines(lines):
    print("Lines entered:")
    for line in lines:
        print(line)

lines = read_multiple_lines()

print_lines(lines)
