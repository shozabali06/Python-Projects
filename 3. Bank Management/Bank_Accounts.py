class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, balance, name):
        if balance >= 0:
            self.name = name
            self.balance = balance
            print(f"\nAccount '{self.name}' created.\nBalance ${self.balance}")
        else:
            print("Sorry, balance can't be negative")

    def getBalance(self):
        try:
            print(f"\nAccount: {self.name}\nBalance: ${self.balance}")
        except AttributeError:
            print("Sorry, this account doesn't exist.")

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"Sorry, Balance low"
            )

    def deposit(self, amount):
        try:
            self.balance = self.balance + amount
            print(f"\nAmount deposited successfully.\nNew Balance is ${self.balance}")
        except AttributeError:
            print("Sorry, this account doesn't exist.")

    def withdraw(self, amount):
        try:
            try:
                self.viableTransaction(amount)
                self.balance -= amount
                print(f"\nWithdraw successful.\nRemaining balance = ${self.balance}")
            except BalanceException as error:
                print(f"\nWithdraw unsuccessful.\n{error}")
        except AttributeError:
            print("Sorry, this account doesn't exist.")

    def __str__(self):
        return f"{self.name}"

    def transfer(self, amount, account):
        try:
            try:
                self.viableTransaction(amount)
                self.balance = self.balance - amount
                account.balance += amount
                print(f"${amount} transferred to {str(account)}")
            except BalanceException as error:
                print(f"\nTransaction unsuccessful.\n{error}")
        except AttributeError:
            print("Sorry, this account doesn't exist.")

class interestAccount(BankAccount):
    try:
        def deposit(self, amount):
            self.balance += amount * 1.05
    except AttributeError:
            print("Sorry, this account doesn't exist.")
    
class savingsAccount(interestAccount):
    def __init__(self, balance, name):
        super().__init__(balance, name)
        self.fee = 5
    
    def withdraw(self, amount):
        try:
            try:
                self.viableTransaction(amount + self.fee)
                self.balance -= amount + self.fee
                print(f"\nWithdraw successful.\nRemaining balance = ${self.balance}")
            except BalanceException as error:
                print(f"\nWithdraw unsuccessful.\n{error}")
        except AttributeError:
            print("Sorry, this account doesn't exist.")