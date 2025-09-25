import string
import datetime
 
def encode(input_text, shift):
 
    alphabet = list(string.ascii_lowercase)
 
    encoded = []
    for letter in input_text:
        if letter.isalpha():
            lowercase = letter.lower()
            orig_index = alphabet.index(lowercase)
            new_index = (orig_index + shift) % 26
            newletter = alphabet[new_index]
            encoded.append(newletter)
        else:
            encoded.append(letter)
 
    return (alphabet, "".join(encoded))
 
def decode(input_text, shift):
 
    alphabet = list(string.ascii_lowercase)
 
    decoded = []
    for letter in input_text:
        if letter.isalpha():
            lowercase = letter.lower()
            orig_index = alphabet.index(lowercase)
            new_index = (orig_index - shift) % 26
            newletter = alphabet[new_index]
            decoded.append(newletter)
        else:
            decoded.append(letter)
 
    return ("".join(decoded))
 
 
import datetime
 
class BankAccount():
    def __init__(self, name = "Rainy", ID = "1234", creation_date = None, balance = 0):
 
        if creation_date is None:
            creation_date = datetime.date.today()
 
        if creation_date > datetime.date.today():
            raise Exception("Date cannot be in the future.")
 
        self.name = name
        self.ID = ID
        self.creation_date = creation_date
        self.balance = balance
 
    def deposit(self, amount):
        if amount < 0:
            print("Deposit amount cannot be negative.")
            return self.balance
  
        self.balance += amount
        print(f"Deposit complete. New balance is {self.balance}.")
        return self.balance
 
    def withdraw(self, amount):
        if amount < 0:
            print("Withdraw amount cannot be negative.")
            return self.balance
        
        self.balance -= amount
        print(f"Withdrawal complete. New balance is {self.balance}.")
        return self.balance
 
    def view_balance(self):
        print(f"Current balance is {self.balance}.")
        return self.balance
 
class SavingsAccount(BankAccount):
    def __init__(self, name = "Rainy", ID = "1234", creation_date = None, balance = 0):
        super().__init__(name, ID, creation_date, balance)
 
    def withdraw(self, amount):
        
        if amount < 0:
            print("Withdraw amount cannot be negative.")
            return self.balance
        
        account_date = (datetime.date.today() - self.creation_date).days
        if account_date < 180:
            print("Withdrawal is not permitted because account is less than 180 days old.")
            return self.balance
 
        if amount > self.balance:
            print("Overdrafts are not permitted.")
            return self.balance
            
        self.balance -= amount
        print(f"Withdrawal complete. New balance is {self.balance}.")
        return self.balance

   
class CheckingAccount(BankAccount):
    def __init__(self, name = "Rainy", ID = "1234", creation_date = None, balance = 0):
        super().__init__(name, ID, creation_date, balance)
 
    def withdraw(self, amount):
        if amount < 0:
            print("Withdraw amount cannot be negative.")
            return self.balance
        
        if self.balance - amount < 0:
            self.balance -= (amount + 30)
            print("Overdraft fee of $30 has been deducted.")
        else:
            self.balance -= amount
        
        print(f"Withdrawal complete. New balance is {self.balance}.")
        return self.balance