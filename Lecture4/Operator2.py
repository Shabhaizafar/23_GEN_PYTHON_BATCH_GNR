# 2) Comparison : <,<=,>,>=,==,!=

# num1 = 12
# num2 = 13

# print(num1<num2)
# print(num1<=num2)
# print(num1>num2)
# print(num1>=num2)
# print(num1==num2)
# print(num1!=num2)

####################################
# 3) Assignment : =,+=,-=,*=,/=,%=,//=

# num1 = 12
# num3 = 14
# num3+=num1 # num3 = num3+num1
# num3-=num1
# num3*=num1
# num3/=num1
# print(num3)#.833

# num3//=num1
# print(num3)#0
# num3%=num1
# print(num3)#1

######################################
# 4) Logical : and  , or  , not 

# num1 = 12
# num2= 13

#        true          true
# print(num1<num2 and num1!=num2)#True
# #       false         true
# print(num1>num2 and num1!=num2) #False

# print(num1>num2 or num1==num2)

# print(not(num1<num2))

####################################################
# 5) special : is , in 

# is Operator : 
# it checks whether the two operands are identical or not .

# num1 = "12"
# num2 = "12"

# print(num1==num2)

# num1 = "zafar"
# num2 = "z"
# print(num1 is num2) # False

# myTuple = (1,2,3,4)

# print(1 is 1)#SyntaxWarning: "is" with 'int' literal. Did you mean "=="?print(1 is 1)


#in Operator 
# It returns True if a specified value is present in the sequence (tuple, list, string), otherwise False.

# myTuple = (1,2,3,4)

# myTuple2 = (1,3)
# print(1,3 in myTuple)