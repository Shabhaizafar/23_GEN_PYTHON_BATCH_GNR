# myList = []
# myList = [1,2,3,4,5]
# print(myList)
# print(type(myList))

# myList = [1,1,2,9,3,4,56,3,11,3,6]

# myList[0] = 100
# myList.sort()
# myList.append(12)
# myList.append(10000)
# myList.reverse()
# myList.remove(3)
# print(myList.index(56))


# 1) Changable
# 2) Add/Remove elements
# 3) Ordered collection of items (elements have a definite order)(sorting)
# Accessing Elements - Indexing


# for i in myList:
#     if(myList.index(i)>5):
#         myList.remove(3)
# print(myList)


####################################################################
# 6. Write a Python program to count the number of even and odd numbers in a series of numbers
# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
# Expected Output :
# Number of even numbers : 5
# Number of odd numbers : 4
 #################################################

#  8. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# Note : Use 'continue' statement.
# Expected Output : 0 1 2 4 5
#################################################
# 9. Write a Python program to get the Fibonacci series between 0 and 50.
# Note : The Fibonacci Sequence is the series of numbers :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number is found by adding up the two numbers before it.
# Expected Output : 1 1 2 3 5 8 13 21 34

n1 = 0
n2 = 1
myList = []
for i in range(0,50):
    n3 = n1+n2
    if(n3<50):
        myList.append(n3)
        n2 = n1 
        n1 = n3 
print(myList)



#1  1   2
#################################################
# 12. Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output (all characters in lower case).
#################################################

# 14. Write a Python program that accepts a string and calculates the number of digits and letters.
# Sample Data : Python 3.2
# Expected Output :
# Letters 6
# Digits 2
#################################################
# 15. Write a Python program to check the validity of passwords input by users.
# Validation :

# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.
#################################################
# 31. Write a Python program to calculate a dog's age in dog years.
# Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.
# Expected Output:

# Input a dog's age in human years: 15                                    
# The dog's age in dog's years is 73
#######################################
# 33. Write a Python program to convert a month name to a number of days.
# Expected Output:

# List of months: January, February, March, April, May, June, July, August
# , September, October, November, December                                
# Input the name of Month: February                                       
# No. of days: 28/29 days 