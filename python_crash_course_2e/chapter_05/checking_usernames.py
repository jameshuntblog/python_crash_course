# checking_usernames.py

current_users = ['James','Duke','John','Kathleen','Laser']
new_users = ['Fred','Joe','Danny','Justin','John','Laser']

current_users_lower = [x.lower() for x in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"{new_user.title()} is already in use. You will need to enter" \
            " a new username.")
    else:
        print(f"{new_user.title()} is an available username.")