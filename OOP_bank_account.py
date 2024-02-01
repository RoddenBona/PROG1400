"""
Author: Rodden Bona
Student ID: W0461260
Course: PROG1400
Respository: https://github.com/RoddenBona/PROG1700
Project: Object Oriented Programming: Bank Account
Programming Language: Python 3
Version: 1
"""
"""
#Thus function will create a bank account with a starting balance of 0 within a dictionary
def create_account(owner, balance=0):
    return {"owner": owner, "balance":balance}

#Check for an account and adds the designated amount of money to add to it
def deposit(account, amount):
    account["balance"] += amount
    print(f"Desposited ${amount}. New balance: ${account['balance']}")

#Check for account and removes the designated amount of money from it
    #provided it has enogh to take from
def withdraw(account, amount):
    if amount <= account["balance"]:
        account["balance"] -= amount
        print(f"Withdrew ${amount}. New balance: ${account['balance']}")
    else:
        print("Insufficient funds")

#Simply will display the account you searched for
def display_balance(account):
    print(f"Account owner: {account['owner']}, Balance: ${account['balance']}")


#Main

"""

#Up above is the procdeural way of programming
#Now we do the Object oriented way of doing it



class BankAccount:
#constructor (__init__method)
#Initilize the attibutes of the class
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

def deposit(self, amount):
    self.balance += amount
    print(f"Deposited ${amount}. New balance: ${self.balance}")

def withdraw(self, amount):
    if amount <= self.balance:
        self.balance -= amount
        print(f"Wothdrew ${amount}. New balnce: ${self.balance}")
    else:
        print("Insufficient funds")

def display_balance(self):
        print(f"Account owner: {self.owner}, Balance: ${self.balance}")


account1 = BankAccount("Rodden")

deposit(account1, 500)

withdraw(account1, 230)

display_balance(account1)

withdraw(account1, 300)