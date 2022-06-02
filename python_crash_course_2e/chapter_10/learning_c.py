# learning_c.py

file_path = 'C:\\Users\\James Hunt\\Documents\\GitHub\\python_learning\\'\
    'python_crash_course_2e\\chapter_10\\learning_python.txt'

# Print the contents once by reading the entire file.
with open(file_path) as file_object:
    contents = file_object.read()
    contents = contents.replace('Python', 'C')
print(contents.rstrip())

# Print the contents once by looping over the file object.
with open(file_path) as file_object:
    for line in file_object:
        line = line.replace('Python', 'C')
        print(line.rstrip())

# Print the contents once by storing the lines in a list and then working with
# them outside the with block.
new_lines = []
with open(file_path) as file_object:
    lines = file_object.readlines()
    for line in lines:
        new_line = line.replace('Python', 'C')
        new_lines.append(new_line)

for new_line in new_lines:
    print(new_line.rstrip())