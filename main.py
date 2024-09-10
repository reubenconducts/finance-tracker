import time 
from timeit import timeit 
import json 
import os
import ledger

def help() -> str:
    print("\nAvailable commands are:")
    print('     "open": open ledger')
    print('   "create": create new ledger')
    print('     "copy": copy ledger to other')
    print('      "add": add a transaction to the ledger')
    print('   "remove": remove a transaction from the ledger')
    print('"visualize": ')
    print('     "exit": exit program')
    
def add():
    print("Add a transaction:")
    # start by getting the kind of the transaction: is it an expense, income, or transfer?
    while True:
        kind = input("What kind of transaction?\n> ")
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
            print('Available kinds are: "income" or "i", "expense" or "e", and "transfer" or "t". Please try again')
            
    # now, get the amount of the transaction and convert it to a float
    amount = input(f"\nWhat is the amount of the {kind}? Please enter as a decimal or a dollar amount\n> ")
    amount = amount.replace(' ', '')
    amount = amount.replace('$', '')
    amount = float(amount)
    print(f"The amount you entered is: ${amount:.2f}")

def main():
    while True:
        command: str = input("\nWhat is your command?\n> ")
        command = command.strip()
        command = command.lower()
        if command == "exit":
            exit()
        elif command == "help":
            help()
        elif command == "add":
            add()
        elif command == "open":
            pass 

if __name__ == '__main__':
    main()