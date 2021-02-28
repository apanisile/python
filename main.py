from existing_user import *
from user_details import *

print ("""Press (1) if you are you a new user 
Press (2) an existing user? """)
user_type = input("> ")

if (user_type == "1"):
    username = input("""Please enter the username you would like to use
    > """)
    print (username)
    user_pin = input("""Please enter a pin you would like to use
    > """)
    if (len(user_pin) != 5):
        print("Please enter a 5 digit pin")
    else:
        print("Great!")

elif (user_type == "2"):
    old = existing_user()
    old.old_user()
    