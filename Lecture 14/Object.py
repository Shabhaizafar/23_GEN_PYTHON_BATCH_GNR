# # class  (simple) 
# # multiple Objects


# class Employees:
#     companyname = "XYZ"
#     def __init__(self,fname,Age):
#         self.FirstName = fname
#         self.Age = Age

#     def __str__(self):
#         return f"Your name is {self.FirstName}.and Your Age is {self.Age}."
    
#     def Leave(self):
#         print("Employee has left the company.")


# # emp1 = Employees(20,"john")

# # print(emp1.FirstName)
# # print(emp1.Age)

# # print(emp1)



# # Your Name is John.and Your Age is 20.

# # emp1.Leave()

# # print(emp1)
# # print(emp1.__str__())
# emp1= Employees("Raj",1)
# emp2=Employees("Tom",35)

# print(emp1.companyname)
# print(emp2.companyname)

# print(emp1.FirstName)
# print(emp2.FirstName)


# emp1.FirstName = "Changer"
# print(emp1.FirstName)
# print(emp2.FirstName)

# emp1.companyname = "ABC"
# print(emp1.companyname)
# print(emp2.companyname)



# n1 = 12
# print(n1)       #12
# print(id(n1))   #140710354172696

# n1 = 13 
# print(n1)      #13
# print(id(n1))  #140710354172728

# n2=13
# print(n2)      #13
# print(id(n2))  #140710354172728

# n2 = 12 
# print(n2)      #12
# print(id(n2))  #140710357187352

#######################################################################
# Practice Question List for Object/Class using  __init__,__str__,and user defined methods :
"""
1. Create a class Employee with attributes FirstName, LastName and ID. Provide appropriate access methods (getters). Also provide a method called display_employee which returns the details of an employee
in the format: “Employee Name: John Doe ,ID: 123”.

2. Modify your code to include a company attribute in the Employee class. The company attribute should be set by calling a separate function that prompts the user to enter this information. This function should return an object of type Company.
"""