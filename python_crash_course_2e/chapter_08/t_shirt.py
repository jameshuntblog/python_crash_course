# t_shirt.py

def make_shirt(size,message_text):
    print(f'You have specified a {size.title()}-size shirt with '\
        f'"{message_text}" printed on it.')

make_shirt("Large","Cool")
make_shirt(size="Large",message_text="Cool")