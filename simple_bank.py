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

with open("database.txt") as file:
    data = eval(file.read())

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
                    amount = int(input("Amount:\n>"))

                    if amount >= user_detail["balance"]:
                        print("Sapa dey")
                    
                    else:    
                        user_detail["balance"] -= amount
                        
                        record = {
                            "amount" : amount,
                            "type" : "debit",
                            "action" : "withdrawal",
                            "date" : datetime.now().strftime('%d-%b-%Y, %H:%M:%S'),
                        }
                        
                        user_detail['transactions'].append(record)
                        
                        print("Withdrawal successful\n")
                            
                elif action == "3":
                    beneficiary_account = input("Enter recipient account number:\n>")
                    amount = int(input("Amount\n>"))
                    
                    beneficiary =  data.get(beneficiary_account)
                    
                    if beneficiary:
                        
                        if amount >= user_detail["balance"]:
                            print("Insufficient funds")
                        
                        else:
                            print(f"Please confirm transfer of ${amount} to {beneficiary['name']}")
                            confirm = input("yes/no: ").lower()
                            
                            if confirm == 'yes':
                                user_detail["balance"]-= amount
                                record = {
                                    "amount" : amount,
                                    "type" : "debit",
                                    "action" : f"transfer to {beneficiary['name']}",
                                    "date" : datetime.now().strftime('%d-%b-%Y, %H:%M:%S'),
                                }
                                
                                user_detail['transactions'].append(record)
                                
                                beneficiary["balance"]+= amount
                                record = {
                                    "amount" : amount,
                                    "type" : "credit",
                                    "action" : f"transfer from to {user_detail['name']}",
                                    "date" : datetime.now().strftime('%d-%b-%Y, %H:%M:%S'),
                                }
                                
                                beneficiary['transactions'].append(record)
                                print("Transfer successful\n")
                        
                    else:
                        print("Invalid recipient account number.")
                
                elif action == "4":
                    records = user_detail['transactions']
                    
                    if len(records) == 0:
                        print("No data to display")
                        
                    else:
                        
                        for record in records[-5:]:
                            
                            print("============================")
                            print(f"Amount: ${record['amount']}")
                            print(f"Transaction Type: {record['type'].title()}")
                            print(f"Action: {record['action'].title()}")
                            print(f"Date: {record['date']}")
                            print("============================\n")
                        print(f"Your balance as at {datetime.now().strftime('%d-%b-%Y, %H:%M:%S')} is ${user_detail['balance']}\n")
                           
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



with open("database.txt", "w") as file:
    file.write(str(data))
    
    
    
    


    
    
    
    
    
        
    
        