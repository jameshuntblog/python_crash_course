# hello_admin.py

user_names = ['admin','James','Duke','John','Kathleen','Bonnie','Vanna',
'Laser']

for user_name in user_names:
    if user_name == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user_name.title()}, thank you for logging in again.")