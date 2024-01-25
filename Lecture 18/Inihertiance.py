# what is  Hybrid Inheritance in a Python : 

# Hybrid inheritance, also known as multi-inheritance or mixed inheritance, is a programming technique
# where a class can inherit from more than one parent classes. This allows for the reuse of code
# from multiple sources while still providing additional functionality specific to each parent.

"""
# Main Class :                    A       
#                                 |
#                _________________|________________
#               |                                 |
# Sub Class :   B-------------------------------- D
#         inherit A                             Inherit(A,B)     

Example 2:
# Main Class :                  A       
#                                 |
#                _________________|________________
#               |                                 |
# Sub Class :   B                                 D
#               |                                 |
#               -----------------------------------
#                                 |
# Child Class:                    C
# """

# Main Class 
class GrandFather:
    def __init__(self,gname):
        self.GrandFatherName = gname

# Sub Class :
class Father(GrandFather):
    def __init__(self,fname,gname,cname):
        super().__init__(gname)
        self.FatherName = fname
        self.ChildsName = cname

class Child(Father,GrandFather):
    def All(self):
        print(f"My Name is {self.ChildsName}")
        print(f"My Father's Name is {self.FatherName}")
        print(f"My Grandfather's Name is {self.GrandFatherName}")
       



# obj1 = Father("Raj","Ajay")
# print(obj1.GrandFatherName,"\n", obj1.FatherName)

obj2 = Child("Atul","Ajay","Raj")

obj2.All()

    

# class Girl(Father):
#     def __init__(self,gsname,fname,gname):
#         super().__init__(fname,gname)
#         self.GirlName = gsname
# obj = Boy("Raj",'Ajay',"Vijay")

# print(obj.BoyName)
# print(obj.FatherName)
# print(obj.GrandFatherName)

# obj2 = Girl("Geeta","Ajay","Vijay")
# print("\n")
# print(obj2.GirlName)
# print(obj2.FatherName)
# print(obj2.GrandFatherName)


# Practice Question list of Hybrid Inheritance : 
"""
Ques 1: Design a class named "Employee" with attributes like EmployeeID, Name,
Designation and Salary. Write a method that will display the details of an employee.
Write another method to increase the salary by 5% using inheritance.

Ques 2: A company has two types of employees - Manager and Employee. The manager
has additional attribute Department while Employee does not have any such attribute.
Design classes for both Manager and Employee accordingly. Now derive a new class from
Manager which should be named as "ProjectManager". ProjectManager should also have an
additional attribute called "ProjectsHandled" which stores number of projects handled by the project manager. Fill the base class methods first and then fill derived class
additional attribute called "ProjectsHandled" which stores number of projects handled by the project manager. Fill in the code for this class.
Now create objects of both Manager and Employee. Create objects of ProjectManager.
Display the details of all three types of employees."""


