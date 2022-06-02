# pi_string.py
import math

file_path = 'C:\\Users\\James Hunt\\Documents\\GitHub\\python_learning\\'\
        'python_crash_course_2e\\chapter_10\\pi_million_digits.txt'

with open(file_path) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
        pi_string += line.strip()

# print(f"{pi_string[:52]}...")
# print(len(pi_string))

birthday = input("Enter your birthday, in the form of mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")