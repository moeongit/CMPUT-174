# A class is a template or a blue print
# A class is same as a type. just like int, float, list etc, we can define our own type
# User Defined Class or User Defined Type - Properties and Behavior of group of objects

class Account:
    # The first method that goes in the class is called the __init__ # 2 __ after and __ before
    # Purpose of the __init__ method is to initialize the instance attibutes of an object
    # Instance Attributes - Instance <-> Object -- Properties 
    def __init__ (self, acc_id, acc_balance):
        # - self is an identifier used by the class to refer to the object
        # - self is the Account object - type of self is Account
        self.account_number = acc_id
        self.account_balance = acc_balance

    # Behaviour of objects are defined by methods in the class
    # Method is a function defined inside the class
    # The first parameter of a method is always self
    def display(self):
        print(f"Account Number: {self.account_number} Balance: ${self.account_balance}")
    def deposit(self, amount):
        print(f"Depositing ${amount} to {self.account_number}")
        self.account_balance += amount
    def withdraw(self, amount):
        print(f"Withdrew ${amount} from {self.account_number}")
        if self.account_balance >= amount:
            self.account_balance = self.account_balance - amount
        else:
            print("Withdrawal Unsuccesful - Insufficient Funds")

def main():
    # A class in Python is a callable
    # A class can be called as if it it were a function
    # When we call a class
        # 1. An object is created
        # 2. The __init__ method in the class is implicitly called 

    account_a = Account("SPONGE1234", 150)
    account_a.display()  
    account_a.deposit(30)
    account_a.display()
    account_a.withdraw(150)
    account_a.display()
main()
