from select import select
from threading import active_count

print("Error Handling Working Example Basics")

try:
    payment = float(input("Please enter amount ?"))
    print(f"Entered Amount is : {payment} ")
except ValueError:
    print(f"Invalid Input and we expect a Number Please !")


# Handling Multiple Exceptions

try:
    # Open a File
    file_path= input("Enter file path which you want to upload : ")
    with open(file_path, 'r') as file:
        data=file.read()
        print(f"File Uploaded Successfully ")
except FileNotFoundError:
    print(" Wrong Path and File did not exist !")
except PermissionError:
    print("You don't have Permission to Read the File !")

#Use Finally Block

try:
    file = open('transaction_log.txt','a')
    file.write("Starting New Transactions ... \n")

    amount = float(input("Enter the amount for payment"))
    if amount < 0:
        raise ValueError("Transaction Amount Can't be Negative")
    else:
        file.write(f"Processed Transaction with Amount : {amount}")
        print(f"Transaction of {amount} Completed Successfully !")
except ValueError as ve:
    file.write(f"The entered amount is Invalid and amount is  : {amount} ...\n")
    print(f"The Error is {ve}")
finally:
    file.close()
    print("Transaction file log is closed")


# Use Custom Exception

# Defining a custom exception for insufficient balance
class InsufficientBalanceError(Exception):
    def __init__(self,message="Balance is Insufficient for Withdrawl."):
        self.message = message
        super().__init__(self.message)

class BankAccount:
    def __init__(self,balance):
        self.balance =balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError(f"Attempted to withdraw ${amount}, but only ${self.balance} available.")
        self.balance -= amount
        print(f"Successfully withdrew ${amount}. Remaining balance: ${self.balance}")




# Using the BankAccount class with custom exception
try:
    account = BankAccount(balance=500)
    withdraw_amount = float(input("Enter the Amount to Withdraw : "))
    account.withdraw(withdraw_amount)
except InsufficientBalanceError as e:
    print(e)
except ValueError as ve:
    print(f"Invalid Input , so Please Enter the Valid Amount ")
