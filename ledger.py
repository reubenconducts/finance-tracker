# class implementing a ledger for finance tracker cli 
from datetime import datetime, date

class Account:
    """class representing an account, such as checking, savings, 
    credit card, or investment.
    """
    def __init__(self, nickname: str, starting_balance: float) -> None:
        self.starting_balance = starting_balance
        self.balance = starting_balance
        self.nickname = nickname
    
    def update_balance(self, new_balance: float) -> None:
        self.balance = new_balance
    
    def transfer_from(self, amount: float) -> None:
        self.balance = self.balance - amount 
    
    def transfer_to(self, amount: float) -> None:
        self.balance = self.balance + amount
        
    def __repr__(self) -> str:
        return (f"Account: nickname = {self.nickname}"
            f" starting balance = {self.starting_balance}"
            f" current balance = {self.balance}")
    
    def __str__(self) -> str:
        return f"Account {self.nickname}"
    
    def print_current_balance(self) -> None:
        print(f"Current balance for {self.nickname}: ${self.balance}")
        
class Savings(Account):
    def __init__(self, nickname: str, starting_balance: float, account: int, routing: int) -> None:
        super().__init__(nickname=nickname, starting_balance=starting_balance)
        self.account = account
        self.routing = routing
    
    def __repr__(self) -> str:
        return ("Savings " + super().__repr__() + f"\nAccount: {self.account}, Routing: {self.routing}")

    def __str__(self) -> str:
        return "Savings " + super().__str__() + f"\nAccount number: {self.account}, Routing number: {self.routing}"
    
class Checking(Account):
    def __init__(self, nickname: str, starting_balance: float, account: int, routing: int) -> None:
        super().__init__(nickname=nickname, starting_balance=starting_balance)
        self.account = account
        self.routing = routing
    
    def __repr__(self) -> str:
        return ("Checking " + super().__repr__() + f"\nAccount: {self.account}, Routing: {self.routing}")

    def __str__(self) -> str:
        return "Checking " + super().__str__() + f"\nAccount number: {self.account}, Routing number: {self.routing}"
    
class Investment(Account):
    def __init__(self, nickname: str, starting_balance: float) -> None:
        super().__init__(nickname, starting_balance)

class Transaction:
    def __init__(self, amount: float, account: Account, kind: str, category: str, date=datetime.now().date()) -> None:
        self.amount = amount 
        self.account = account 
        self.category = category 
        self.date = date
        self.kind = kind
    
    # allow for updating of amount of a transaction 
    def update_amount(self, new_amount: float):
        self.amount = new_amount
    
    def update_account(self, new_account: Account):
        self.account = new_account
        
    def __str__(self) -> str:
        return f'Transaction type: {self.kind} | Amount: {self.amount} | Category: {self.category} | Date: {self.date}'
        
class Expense(Transaction):
    """subclass of Transaction representing an expense. adds a target string,
    representing the recipient of the expense.
    """
    def __init__(self, amount: float, account: Account, target: str, category: str, date=datetime.now().date()) -> None:
        super().__init__(amount, account, category, date, kind="expense")
        self.target = target 
        
class Income(Transaction):
    def __init__(self, amount: float, source: str, account: Account, category: str, date=datetime.now().date()) -> None:
        super().__init__(amount, account, category, date, kind="income")
        self.source = source
        
class Transfer(Transaction):
    def __init__(self, amount: float, from_account: Account, to_account: Account, category: str, date=datetime.now().date()) -> None:
        super().__init__(amount, from_account, category, date, kind="transfer")
        self.to_account = to_account 
        
    def update_from_account(self, new_account: Account):
        self.update_account(new_account=new_account)
    
    def update_to_account(self, new_account: Account):
        self.to_account = new_account

class Ledger:
    
    def __init__(self, name: str, accounts: list[Account] = [], date_created=date.today(), transactions: list[Transaction] = []) -> None:
        self.name = name
        self.date_created = date_created
        self.accounts = accounts
        self.transactions = transactions
    
    def add_transaction(self, transaction: Transaction) -> None:
        self.transactions.append(transaction)
    
    def compute_total_balance(self) -> float:
        total = 0
        for transaction in self.transactions:
            if transaction.kind == "expense":
                total -= transaction.amount 
            elif transaction.kind == "income":
                total += transaction.amount 
        return total 

    def __str__(self) -> str:
        string = f"Ledger \"{self.name}\" | Created {self.date_created}" 
        return string

    def full_repr(self) -> str:
        string = f"Ledger \"{self.name}\" | Created {self.date_created}" 
        for transaction in self.transactions:
            string += '\n' + transaction.__str__()
        return string
    
    
class User():
    def __init__(self) -> None:
        pass
    
    