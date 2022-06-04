# programming_poll.py

filename = 'C:\\Users\\James Hunt\\Documents\\GitHub\\python_learning\\'\
    'python_crash_course_2e\\chapter_10\\programming_poll.txt'

response = ''

while response != 'quit':
    response = input("\nIf you wish to exit the program, please input "\
            "'quit'\nOtherwise, Please input the reason you like programming: ")
    if response.lower() == 'quit':
        break
    else:
        print(f"\nThank you for taking our poll!\n")
        with open(filename, 'a') as file_object:
            file_object.write(f"{response}\n")