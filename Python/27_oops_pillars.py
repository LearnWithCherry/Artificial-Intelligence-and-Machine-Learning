'''
1 - Encapsulation (Wrapping data and function into a single unit)
2 - Abstraction 
3 - Inheritance
4 - polymorphism
5 - Access specifier:
                    public - normal variable name "name"
                    protected - add one under score before variable name "_name"
                    private - add two under score before variable name "__name" - to access it we can write objectname._classname__PrivateVariableName
                    
'''
class BankAccount:
    def __init__(self, name, balance, password):
        self.name = name #public
        self._balance = balance #protected      
        self.__password = password

    def get_balance(self): # Getter
        return self.__password
    
    def set_balance(self, newPassword): # Getter
        self.__password = newPassword
acc1 = BankAccount("Rajat", 41000, 1223)
print(acc1.name, acc1._balance, acc1.get_balance())
acc1.set_balance(2234)
print(acc1.name, acc1._balance, acc1.get_balance())


        

