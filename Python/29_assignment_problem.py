class BankAccount():
    def __init__(self, Account_number, Owner_name, Balance):
        self.Account_number = Account_number
        self.Owner_name = Owner_name
        self.Balance = Balance

    def Deposite(self): 
        print(f"Money deposite: {self.deposite}")
    def Withdraw(self):
        print(f"Amount WithDraw: {self.amount}")
    def Check_Balance(self):
        print(f"Current balance: {self.balance}")


        