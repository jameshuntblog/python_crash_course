# large_shirts.py

def make_shirt(message_text,size="Large"):
    print(f'You have specified a {size.title()}-size shirt with '\
        f'"{message_text}" printed on it.')

make_shirt("I love Python.")
make_shirt(message_text="I love Python.",size="Medium")
make_shirt(message_text="Little...Yellow...Different",size="Small")