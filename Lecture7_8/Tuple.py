# Synax  
# myTuple = (1,2,3)
# myTuple = ("zafar","Z")

# myTuple = ()
# # myTuple = (1,2,3,4,5)
# print(myTuple)
# print(type(myTuple))

# myTuple2 = ("Raj","Aarav","Jay")
# print(myTuple2)
# print(type(myTuple2)) 

myTuple = (1,1,2,3,4,1,5,4,3,2,1)
# myTuple[10] =12
# print(myTuple)

# print(myTuple.count(1))
# print(myTuple.index(1))
                # number,starting index,ending index
# print(myTuple.index(1,3,6))

# 1) not Changable 
# 2) not added new Element /delete
# 3) Not sorted
# 4) repeated value Accepted
# Tuples are immutable so we can't add or delete element in tuple but we can change the existing elements of tuple.



for i in myTuple:
    if i%2==0 :
        print("Even Number",i)