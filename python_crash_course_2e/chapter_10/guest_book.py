# guest_book.py

filename = 'C:\\Users\\James Hunt\\Documents\\GitHub\\python_learning\\'\
    'python_crash_course_2e\\chapter_10\\guest_book.txt'

response = ''

while response != 'quit':
    response = input("\nIf you wish to exit the program, please input "\
            "'quit'\nOtherwise, Please input your full name (First Last) for "\
            "our guest book: ")
    if response.lower() == 'quit':
        break
    else:
        print(f"\nWelcome, {response.title()}\n")
        with open(filename, 'a') as file_object:
            file_object.write(f"{response}\n")