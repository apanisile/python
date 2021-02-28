from existing_user import *
from user_details import *

print ("""Press (1) if you are you a new user 
Press (2) an existing user? """)
user_type = input("> ")


if (user_type == "1"):
    new = new_user()
    new.new_user()
    user = loan_function()
    user.name()
    user.email()

    print("Your credit core should be more than $500 to qualify for our loan")
    bank_credit = int(input("Please what is your bank credit score: "))

    bench_mark = 500

    if bank_credit >= bench_mark:
       user.payment()
       print("Your account would be credited in the next 2-5 working days")

    else:
        print(f"Sorry! You do not qualify for our bank loan")
        exit(1)



elif (user_type == "2"):
    old = existing_user()
    old.old_user()
    