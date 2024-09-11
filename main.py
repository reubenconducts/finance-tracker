import time 
from timeit import timeit 
from datetime import datetime, date
import json 
import os
import ledger as ld

def help() -> str:
    print("\nAvailable commands are:")
    print('     "open": open ledger')
    print('   "create": create new ledger')
    print('     "copy": copy ledger to other')
    print('      "add": add a transaction to the ledger')
    print('   "remove": remove a transaction from the ledger')
    print('"visualize": ')
    print('     "exit": exit program')
    
def add_trans():
    print("Add a transaction:")
    # start by getting the kind of the transaction: is it an expense, income, or transfer?
    while True:
        kind = input("\nWhat kind of transaction?\n> ")
        if kind == "expense" or kind == "e":
            kind = "expense"
            break
        elif kind == "income" or kind == "i":
            kind = "income"
            break
        elif kind == "transfer" or kind == "t":
            kind = "transfer"
            break
        else: 
            print('\nAvailable kinds are: "income" or "i", "expense" or "e", and "transfer" or "t". Please try again')
            
    # now, get the amount of the transaction and convert it to a float
    amount = input(f"\nWhat is the amount of the {kind}? Please enter as a decimal or a dollar amount\n> ")
    amount = amount.replace(' ', '')
    amount = amount.replace('$', '')
    amount = float(amount)
    print(f"The amount you entered is: ${amount:.2f}")
    
    # get the account from which the transaction came
    account = input(f"\nFrom which account did the transaction come?\n> ")
    
    # now, get the category of the transaction. eventually, include functionality to add categories that don't yet exist in the ledger.
    category = input(f"\nWhat is the category of the transaction?\n> ")
    
    # now, get the date of the transaction
    while True:
        try: 
            trans_date = input(f"\nWhen did the transaction take place? You may write 'today' or the date in ISO format as YYYY-MM-DD\n> ")
            if trans_date == "today":
                trans_date = date.today()
            else:
                trans_date = date.fromisoformat(trans_date)
            break
        except ValueError:
            print("\nThat is an invalid input. Please try again.")
            
    print(f"\nThe transaction took place {trans_date}")
    
    return ld.Transaction(amount=amount, account=account, kind=kind, category=category, date=trans_date)

def main():
    ledger = ld.Ledger(name="base")     
    print(f"The current ledger is {ledger}") 
    while True:
        command: str = input("\nWhat is your command?\n> ")
        command = command.strip()
        command = command.lower()
        if command == "exit":
            exit()
        elif command == "help":
            help()
        elif command == "add":
            new_trans = add_trans()
            ledger.add_transaction(new_trans)
        elif command == "show":
            print(ledger.full_repr())
        elif command == "open":
            pass 

if __name__ == '__main__':
    main()