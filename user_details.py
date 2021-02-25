# Module containing all the functions to be used
class loan_function:

    def greet(fname, lname, msg="Good morning!"):
        """
        This function greets to
        the person with the
        provided message.

        If the message is not provided,
        it defaults to "Good
        morning!"
        """
        print("Hello", fname + ' '+ lname + ', ' + msg)
        
    def name(self):
        fname = input("Hi there! Please enter your first name: ")
        lname = input("Please enter your last name: ")

        loan_function.greet(lname, fname)
        
    def validate_numbers(x, y):
        
        if x != y:
            print("The numbers entered are not the same")
            exit(1)
        else: 
            print("Accepted")
            

    def email(self):
        email = input("Enter your e-mail address: ")
        email1 = input("Enter your e-mail address again: ")
        
        def validate_email(x, y):
            if email != email1:
                print("The email's dont match")
                exit(1)
        
        validate_email(email, email1)

    def payment(self):
        
        print("Great! you qualify for a loan! ")
        print("What payment method would you prefer: ")
        
        payment_method= int(input("""
        1. Direct Deposit
        2. Wire Check
        3. Transfer 
        > """))
        
        if payment_method == 1:
            
            print("You have chosen the dircet deposit option")
            
            bank_name = input("Enter bank name: ")

            routing_no = input("Enter your routing number: ")
            routing_no1 = input("Enter your routing number again: ")
            loan_function.validate_numbers(routing_no, routing_no1)
            
            acct_no = input("Enter your account number: ")
            acct_no1 = input("Enter your account number again: ")
            loan_function.validate_numbers(acct_no, acct_no1)
            
        elif payment_method == 2:
            print("You have chosen the Wire Check option")
            account_name = input("What name should be written on the check?: ")
            
        elif payment_method == 3:
            print("You have chosen the transfer option!")
        else:
            print("There is no option like that")
            exit(1)
            