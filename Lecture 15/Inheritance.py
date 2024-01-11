# What is Inheritance in a Python : 
# Inheritance is the ability of one class to inherit properties and methods from another class

# # Parent Class
# class Person:
#     def __init__(self,fname,lname,Age):
#         self.firstName = fname
#         self.lastName = lname
#         self.age = Age
    
#     def FullName(self):
#         print(f"Your Name is {self.firstName} {self.lastName}.and your age is a {self.age}.")

# parent = Person("Raj","Shah",10)

# parent.FullName()


# # Child Class
# class Child(Person):
#     pass


# child1 = Child("Jay","Patel",100)

# child1.FullName()

# print(child1.firstName)

############################
# # Parent Class
# class Person:
#     def __init__(self,fname,lname,Age):
#         self.firstName = fname
#         self.lastName = lname
#         self.age = Age
    
#     def FullName(self):
#         print(f"Your Name is {self.firstName} {self.lastName}.and your age is a {self.age}.")

# # Child Class
# class Child(Person):
#     def __init__(self,fname,lname,Age,School):
#         # self.Fn  = fname
#         # self.firstName  = fname
#         # self.lastName  = lname
#         # self.age = Age
#         self.school = School

# child1 = Child("Jay","Patel",1,"ABC")

# child1.FullName()

##################################
# Parent Class
# class Person:
#     def __init__(self,fname,lname,Age):
#         self.firstName = fname
#         self.lastName = lname
#         self.age = Age
    
#     def FullName(self):
#         print(f"Your Name is {self.firstName} {self.lastName}.and your age is a {self.age}.")

# # Child Class
# class Child(Person):
#     def __init__(self,fname,lname,Age,School):
#         Person.__init__(self,fname,lname,Age)
#         self.school = School
        
# Child Class
# class Child(Person):
#     def __init__(self,fname,lname,Age,School):
#         super().__init__(fname,lname,Age)
#         self.school = School
#     def FullName(self):
#         print("XYZ")

# child1 = Child("Jay","Patel",1,"Abc")

# child1.FullName()

# print(child1.school)


# Practice Question List for Object/Class using Inheritance :
"""
1. Create a base class called "Animal" with attributes like name, color and species.
Derive two classes from it - "Dog" and "Cat". Each should have the
attributes height, weight and breed. Implement a method to speak() in both
classes which prints "Hello I am <animal_type>." (e.g., Hello
I'm a Dog). Derive another class "Lion" from Animal but do not add
anything extra to it. Then create objects of each type and call their
speak() methods.
--------------------------------
2. A company has employees who work different shifts. The shift types are
MondayShift, TuesdayShift etc. Write a Python code that represents an Employee
class with attributes like first name, last name and role. Also write a Shift
class representing working shift with attributes like start time, end time
and day of week. Finally represent EmployeesWorking class which holds a list
of EmployeeWorking objects where each object contains an employee and his
working shift. You need to implement a method getEmployeesByShift() in
EmployeesWorking class which returns all the employees who works on a given
shift.

--------------------------------------------
3. Design a BankAccount class with attributes like account number, balance and interest rate.
Also design a SavingsAccount class derived from BankAccount class with additional attribute annual fee.
Implement a deposit() method in BankAccount class which adds amount to the balance.
Add withdrawal() method which subtracts specified amount from the balance.
Write a check() method which generates a check with details of account holder,
account number, current balance.
 Add a payInterest() method in
BankAccount class which calculates and pays interest on the account balance.

In SavingsAccount class also include this method along with a depositSavings()
method which accepts amount as parameter and deducts annual fee from it before adding amount to savings balance.
method which accepts amount as parameter and increases the balance by adding
amount plus 5% of amount as annual charge. Withdrawal from savings account is
not allowed.
"""

