# def Functionanme(perameter):
    # statement 
# FunctionCalling()


# Lamda Function 

#  only single Statement

# syntax  
# myfu = lambda perameter : statement 


# single perameter
# myfu = lambda a : a+a

# print("Ans is  : ",myfu(5)) # 10

# two Perameter 

# myfu2 = lambda a,b : a+b 

# print("Ans is  : ", myfu2(1,2))

# myfu2 = lambda a,b,c : a+b-c 

# print("Ans is  : ", myfu2(1,2,10))




# what is  Anonymous Function :
"""
An anonymous function, also known as an inline function or a one-liner function, is a function that is defined without a name
"""
# num1 = int(input("Enter the Value of Num1 :"))
# num2 = int(input("Enter the Value of Num2 :"))

num1 = 12
num2 = 34
print("\n1 for Addition.")
print("\n2 for Subtraction.")
print("\n3 for Multiplication.")
print("\n4 for Division.")
def  Operation(n2):
    your_choice = int(input("Enter your Choice : "))

    if(your_choice == 1):
        return lambda n1 :  n1+n2
    elif(your_choice == 2):
        return lambda n1 :  n1-n2
    elif(your_choice == 3):
        return lambda n1 :  n1*n2
    elif(your_choice == 4):
        return lambda n1 :  n1/n2
    else:
        pass 


ouput = Operation(num2)
print("Ans is : ",ouput(num1))



lambda n1,n2 : n1+n2
