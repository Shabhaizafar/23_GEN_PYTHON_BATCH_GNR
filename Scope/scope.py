# Scope : 
# 1) Local Scope 
# def local_scope():
#     num1 = 12
#     print(num1)

# local_scope()

# def local_scope2():
#     print(num1)
# local_scope2()
###############################
# 2) Global Scope 

# num1 = 12

# def global_scope():
#     print(num1)
# global_scope()

# def global_scope2():
#     print(num1)
# global_scope2()

###############################

# def convertor():
#     global num1
#     num1 = 12
#     print(num1)

# convertor()

# def convertor2():
#     print(num1)

# convertor2()

# print("Outer :",num1)