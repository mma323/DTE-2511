while True:
    try:
        file_name = input("Enter a filename: ")
        file = open(r"{}".format(file_name), "r") #\ har betydning i filnavn
    except FileNotFoundError:
        print("File not found")
    else:
        break

old_string = input("Enter the old string to be replaced: ")
new_string = input("Enter the new string to replace the old string: ")

new_lines = []
for line in file:
    new_line = line.replace(old_string, new_string)
    new_lines.append(new_line)

file.close()

file = open(r"{}".format(file_name), "w")

file.writelines(new_lines)
print("Done")
file.close()