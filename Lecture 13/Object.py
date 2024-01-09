# class myClass:
#     num1 = 12

# print(myClass)
# print(myClass())

# myobj1 = myClass()

# print(myobj1.num1)
    
##########################################
# class myClass:
#     x = 12  #  Class Attribute 
#     def __init__(self):
#         x = 12  # not Accessable # error
# myobj = myClass()

# print(myobj.x)

########################################
# class myClass:
#     def __init__(self):
#         print("zafar") # not for object 
#         return "Zafar" # Error 

# myobj = myClass()

# print(myobj.__init__())
#######################################
# class myClass:
#     def __init__(self,fname,Age):
#        self.firstname = fname
#        self.Age = Age 
        

# myobj = myClass("Raj",30)  #intilization

# print("Your Name is : ",myobj.firstname)
# print("Your Age is : ",myobj.Age)
################################################
# class Employee:
#     def __init__(zafar,fname,Age):
#         zafar.firstname = fname
#         zafar.age = Age

# e1 = Employee("XYZ",1)

# print(e1.firstname)
# print(e1.age)
##############################################
# class Employee:
#     def __init__(zafar,fname,self):
#         zafar.firstname = fname
#         zafar.age = self

# e1 = Employee("XYZ",1)

# print(e1.firstname)
# print(e1.age)

# class myClass: 
#     x = 12
#     y = 13
#     z = 14

# myobj = myClass()
# print(myobj.x)
# Modify Attribute
# myobj.x  = 100
# print(myobj.x)

# print(myobj.y)
# del myobj.y
# print(myobj.y)

myobj2 = myClass()

# print(myobj2.y)

# print(myobj)
# print(myobj2)

del myobj

# print(myobj)  #error
print(myobj2.x)