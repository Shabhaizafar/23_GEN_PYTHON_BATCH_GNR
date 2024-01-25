# Single Inheritance : 
"""
 Parent Class : A
                |  
 Child Class :  B (inherit All Properties of A)
"""

# Multiple Inheritance : 
"""
Parent Class : (More then 1 Parent Class)
                    A                B
                    |                |
                    ------------------
                            |
Child Class :               C(Inherit All Properties of A and B)

"""

# Multi-level Inheritance : 
"""
Parent 1 :                         A
                                   |
Parent 1 Child (Parent 2) :        B (Inherit All Properties of A)
                                   |
Parent 2 Child :                   C (Inherit All Properties of B)
"""

# class GrandFather: 
#     def __init__(self,gname):
#         self.GrandFathername = gname

# class Father(GrandFather):
#         def  __init__(self,fname,gname):
#              super().__init__(gname)
#              self.Fathername = fname

# class Son(Father):
#      def __init__(self, sname, fname, gname):
#           super().__init__(fname,gname)
#           self.SonName = sname

# s1 = Son("Raj","Ajay Bhai","Atul Bhai")

# print(s1.SonName)
# print(s1.Fathername)
# print(s1.GrandFathername)

# Hierarchical Inheritance :
"""
Parent Class :                  A       (always one parent class and Child Multiple)
                                |
               _________________|________________
              |                 |               |
Child Class : B                 C               D
"""
# class Person:
#     def __init__(self,mname,fname):
#         self.Mothername = mname
#         self.Fathername = fname

# class Girl(Person):
#     def __init__(self,gname,mname,fname):
#         super().__init__(mname,fname)
#         self.Girlname = gname

# class Boy(Person):
#     def __init__(self,bname, mname, fname):
#         super().__init__(mname, fname)
#         self.Boyname = bname 

# G1 = Girl("Geeta","Kunjan","Atul Bhai")
# B1 = Boy("Raj","Kunjan","Atul Bhai")

# print(G1.Girlname)
# print(G1.Fathername)
# print(G1.Mothername)

# print(B1.Boyname)
# print(B1.Fathername)
# print(B1.Mothername)

#######################
# Hybrid Inheritance : 
"""
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
# class A:
#     def __init__(self,x):
#         self.A_var = x

# class B(A):
#     def __init__(self,x,y):
#         super().__init__(self,x)
#         self.B_var = y

# class C(B,A):
#         def all(self):
#              print("DOne")

# obj1 = 


    
    

