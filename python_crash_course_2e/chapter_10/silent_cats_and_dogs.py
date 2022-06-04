# cats_and_dogs.py
filenames = ['cats.txt','dogs.txt','does_not_exist.txt']

def file_reader(filename):
    try:
        for filename in filenames:
            with open(filename) as file_object:
                contents = file_object.read()
                print(contents)
    except FileNotFoundError:
        pass

file_reader(filenames)