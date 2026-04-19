# __init__ method
class Student:
    def __init__(self, name, CGPA):
        self.name = name
        self.CGPA = CGPA

    def get_cgpa(self):
        return self.CGPA
stu1 = Student("Rajat", 7.9)
stu2 = Student("Rohit", 9.0)
stu3 = Student("Rihu", 2.2)


# print(stu1.name, stu1.CGPA)
# print(stu2.name, stu2.CGPA)
# print(stu3.name, stu3.CGPA)

# print(f"{stu1.name} is having {stu1.get_cgpa()} CGPA")


# Inheritance 
class collage:
    startTime = "9 AM"
    endTime = "5 PM"

    def change_time(self, newEndTime):
        self.endTime = newEndTime
class program(collage):
    def __init__(self, program_name):
        self.program_name = program_name

class course(collage):
    def __init__(self, course_name):
        self.course_name = course_name


c = course("AI & ML")
p = program("Computer Science Engineering")
# print(p.program_name)
# print(c.course_name, c.startTime, c.endTime)


'''
super() - to access inheritance class instance

Types of Inheritance: 
        Single level Inheritance
        Multi level Inheritance
        Multiple Inhertance  

'''

# Multi level Inheritance.

class Employee:
    def __init__(self, name, Stime, Etime):
        self.name = name
        self.Stime = Stime
        self.Etime = Etime
        
class AdminStaff(Employee):
    def __init__(self, name, Stime, Etime, defineRole):
        super().__init__(name, Stime, Etime)
        self.defineRole = defineRole

adm = AdminStaff("Rajat", "9 AM", "5 PM", "ML developer")
# print(adm.name, adm.Stime, adm.Etime, adm.defineRole)

# Multiple inheritance

class Teacher:
    def __init__(self, salary):
        self.salary = salary

class Student:
    def __init__(self, GPA):
        self.GPA = GPA
        
class TA(Teacher, Student):
    def __init__(self, salary, GPA, name):
        super().__init__(salary)
        Student.__init__(self, GPA)
        self.name = name


TA1 = TA(20000, 8.9, "Rajat")

# print(TA1.name, TA1.salary, TA1.GPA)


# Abstraction ( Hiding internal details & showing only essiential features (different from data hiding))

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def makeSound(self):
        pass

class Lion(Animal):
    def makeSound(self):
        print("Roaaarrrr....")
        
class Cow(Animal):
    def makeSound(self):
        print("Mooohhhh....")

lion = Lion()
lion.makeSound()

cow = Cow()
cow.makeSound() 

