# imported_admin.py

from users import User
from admin import Admin

my_user_info = Admin("james", "hunt", 39, "united states", "english")

my_user_info.describe_user()
my_user_info.greet_user()
my_user_info.set_login_attempts(40)
my_user_info.increment_login_attempts()
my_user_info.read_login_attempts()
my_user_info.show_privileges()