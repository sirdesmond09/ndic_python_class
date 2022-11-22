"""This is a simple implementation of a fin-tech solution that allows users to:
1. Signup and create an account
2. Make Deposits
3. Withdraw from balance
4. Transfer to other users
5. Request statement of account.
6. Logout from account
"""


import random
import time
from datetime import datetime

data = {}

############ FUNCTIONS ###################

def signup(database):
    
    """Takes a dictionary database, asks the user for inputs then generate an account number and stores the data in the database with the account number as the key.

    Returns:
        database (dict): this is the updated database
    """
    
    name = input("Enter your name: ")
    time.sleep(2)
    address = input("Enter your address: ")
    time.sleep(2)
    phone = input("Enter your phone number: ")
    time.sleep(2)
    pin = input("Enter your 6 digit pin: ")
    time.sleep(2)
    print("Processing account.........")
    time.sleep(4)
    
    # account_number = "0" + "".join([str(random.choice(range(10))) for _ in range(9)])
    
    account_number = "0" + str(random.randrange(100000000, 999999999))
    
    database[account_number] = {
        "name": name,
        "address": address,
        "phone": phone,
        "pin": pin,
        "balance": 50,
        "transactions" : [],
    }
    
    first_name = name.split(" ")[0]
    
    print(f"Dear {first_name},\nYour account has successfully been created. You account number is {account_number} use this for login.")
    return database




##### CODES #################

print("Welcome to the ABC-Bank of Africa")
on = True
while on:
    print("Select l to login or s to signup for an account. \nSelect any other key to quit.")

    selection = input(":> ").lower()

    if selection == "l":
        account_number = input("Account Number:\n>")
        pin = input("Enter your six digit pin:\n>")
        
        user_detail = data.get(account_number)
        
        if user_detail and user_detail['pin'] == pin:
            login = True
            
            while login:
                print(f"Welcome, {user_detail['name']}")
                print(f"Your current balance is ${user_detail['balance']}")
                print("""Please select a course of action:
                    1. Deposit
                    2. Withdrawal
                    3. Transfer
                    4. Statement of Account
                    5. Logout""")
                action = input(":>")
                
                
                if action == "1":
                    amount = int(input("Amount:\n>"))

                    user_detail["balance"] += amount
                    
                    record = {
                        "amount" : amount,
                        "type" : "credit",
                        "action" : "deposit",
                        "date" : datetime.now().strftime('%d-%b-%Y, %H:%M:%S'),
                    }
                    
                    user_detail['transactions'].append(record)
                    
                    print("Deposit successful\n")
                
                elif action == "2":
                    pass
                
                elif action == "3":
                    pass
                
                elif action == "4":
                    pass
                
                elif action == "5":
                    login = False
                    print("Session Ended")
        else:
            print("Invalid authentication details.")
        
    elif selection == "s":
        data = signup(data)
    else:
        print("Bye ):")
        on = False




print("\n\n", data)