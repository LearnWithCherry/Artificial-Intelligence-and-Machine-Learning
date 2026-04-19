# class Student:
#     def __init__(self, name, CGPA):
#         self.name = name
#         self.CGPA = CGPA

#     def getCGPA(self):
#         return self.CGPA
    
# std1 = Student("Rajat",6.5)
# std2 = Student("Ruhi",6.5)
# std3 = Student("Ansh",6.5)

# print(f"{std1.name} has {std1.getCGPA()} CGPA")
# print(f"{std2.name} has {std2.getCGPA()} CGPA")
# print(f"{std3.name} has {std3.getCGPA()} CGPA")

# types of constructor 
'''
default having one argument 
parameterized is having more then 2 or 2 arguments
only one constructor is allowed in python 
'''

# Attributes (class - belong to class and instance - belong to object)

# class Student:
#     collage_name = "LPU" # class attribute 

#     def __init__(self, name, gpa): # instance attribute
#         self.name = name
#         self.gpa = gpa

    
# stu = Student("Rajat",6.5)

# method in python  (instance / class / static)

#instance method
# class laptop:
#     storage_type = "SSD"

#     def __init__(self, ram, storage):
#         self.ram = ram
#         self.storage = storage

#     def get_info(self): 
#         print(f"Laptop has {self.ram} and {self.storage} and storage type is {self.storage_type}")
# l1 = laptop("16GB", "1TB")
# l2 = laptop("32GB", "4TB")

# # l1.get_info()


# class method (can access class method not instance )

# class laptop:
#     storage_type = "SSD"

#     def __init__(self, ram, storage):
#         self.ram = ram
#         self.storage = storage
#     @classmethod
#     def get_type(cls):
#         print(f"storage type is {cls.storage_type}")

#     def get_info(self): 
#         print(f"Laptop has {self.ram} and {self.storage} and storage type is {self.storage_type}")
# l1 = laptop("16GB", "1TB")
# l2 = laptop("32GB", "4TB")

# l1.get_info()
# l2.get_type()

# laptop.get_type()


# static method (no compulsory parameter we use @static method the they does not belong to any class
# they are a stand along method (no self parameter, no class parameter))

# design a product store name and price 

class Store:
    count = 0
    def __init__(self, name, price):
        self.name = name
        self.price = price
        Store.count = Store.count + 1

    def getinfo(self):
        print(f"Name of the product is {self.name} and price is {self.price}")
    @classmethod
    def counting(cls):
        print(f"Total product created: {cls.count}")

    @staticmethod
    def discount(price, percentage):
        print(f"Final Price: {price - (price * percentage / 100)} ")
p1 = Store("Laptop", 150000)
p2 = Store("Phone", 100000)
p3 = Store("Earphone", 10000)

p1.discount(p1.price,100)
