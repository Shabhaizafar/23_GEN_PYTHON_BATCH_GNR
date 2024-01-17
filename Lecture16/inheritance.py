# What is Inheritance in a Python :
# Inheritance is the ability of one class to inherit properties and methods from another class.


# Type of Inheritance in a Python : 
# 1) Single Inheritance 
# print("Hello")
# """
# Parent   :      A 
#                 |
#                 |
# Child    :      B 
# """
# # Parent Class
# class Parent:
#     def fun1(self):
#         print("This Function is a Parent Class Function")

# # Child Class : 
# class Child(Parent):
#     def Fun2(self):
#         print("This Function is a Child Class Function")


# c1 = Child()
# c1.Fun2()
# c1.fun1()
#########################################
# 2) Multiple Inheritance
# """
# Parent   :   M         F 
#              |         |
#              |         |
#              -----------
#                   |
# Child    :        B 
# """
# # # Parent Class
# class Mother:
#     mname  = ""
#     def mother(self):
#         print(self.mname)

# class Father:
#     fname = ""
#     def father(self):
#         print(self.fname)

# # Child Class : 
# class Boy(Mother,Father):
#     def All(self):
#         print("Father Name : ",self.fname)
#         print("Mother Name : ",self.mname)


# raj  = Boy()
# raj.fname = "ABC"
# raj.mname = "XYZ"

# raj.All()
#############################################################
# 3) Multi level Inheritance
# 4) HieraChical Inheritance
# 5) Hybrid Inheritance


# Practice Question list of Multiple Inheritance : 
"""
1) Design a class for a library which has books and members. The library should have methods to
add book , remove book , add member , remove member , display all the books , display all the
members . Each book should have name , author and price . Each member should have name , age
and address . When adding a new book or member it should be added in both books and members
list . When removing from any one list it should reflect in other list as well .
"""