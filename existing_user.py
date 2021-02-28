#Python program to calculate loan

from user_details import *
class existing_user:

        def __init__(self):
                super().__init__()

                
        def old_user(self):
            prompt_user = input("""Do you want to sign in? (Y)es or (N)o 
                > """)


            if (prompt_user == "Y") | (prompt_user == "y") | (prompt_user == "yes") | (prompt_user == "Yes"):

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


            else:
                print("Bye!")
                exit(0)

class new_user:
    def new_user(self):
        username = input("""Please select the username you would like to use
            > """)
        print (username)

        no_of_trials = 3
        for tries in range(no_of_trials):
            user_pin = input("""Please enter a pin you would like to use
            > """)
            if (len(user_pin) != 5):
                print("Please enter a 5 digit pin")
            else:
                print("Great!")
                break