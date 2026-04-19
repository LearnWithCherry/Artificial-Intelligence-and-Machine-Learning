# print(1+2, "Hello"+ " World")
# function overriding (Redefining parent function in child class )

class Employee:
    def get_designation(self):
        print("Designation = Employee")

class Teacher(Employee):
    def get_designation(self):
        print("Designation = Teacher")

t1 = Teacher()
# t1.get_designation()


# duck typing ()
 

class Teacher():
    def get_designation(self):
        print("Designation = Teacher")
        
class Accountant():
    def get_designation(self):
        print("Designation = Accountant")

t1 = Teacher()
t1.get_designation()

a1 = Accountant()
a1.get_designation()