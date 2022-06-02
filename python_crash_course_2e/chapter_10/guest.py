# guest.py

filename = 'C:\\Users\\James Hunt\\Documents\\GitHub\\python_crash_course\\'\
    'chapter_10\\guest.txt'

with open(filename, 'w') as file_object:
    prompt_response = input("Please provide your full name (First Last) for "\
        "our guest book: ")
    file_object.write(f"{prompt_response}\n")