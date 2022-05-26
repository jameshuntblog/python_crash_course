# archived_messages.py

unsent_messages = ["Ron Popeil faked his death.","Aliens are real.",\
    "I know where the beef is located."]
sent_messages = []


def send_messages(list_of_messages):
    while list_of_messages:
        message = list_of_messages.pop()
        print(message)
        sent_messages.append(message)

send_messages(unsent_messages[:])

print(unsent_messages)
print(sent_messages)