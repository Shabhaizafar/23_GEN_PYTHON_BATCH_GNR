# # OS Module Function :
# '''
# - Handling the Current Working Directory
# - Creating a Directory
# - Listing  Files and Directories in a Directory
# - Reading File Contents
# - Writing to a File
# - Appending to a File
# - Deleting Directory or Files using OS Module
# '''
# # Handling the Current Working Directory
# '''os.getcwd()'''
# # import os

# # path1 = os.getcwd()
# # print("CWD : ",path1)


# # Changing the Current Working Directory
# '''os.getcwd()  ,  os.dir()'''
# # import os 
# # def CurrentPath():
# #     print("Current Path : ")
# #     print(os.getcwd())

# # CurrentPath()

# # os.chdir('C:/users/shabh/desktop')
# # CurrentPath()


# # Creating a new Directory : 
# '''os.mkdir(), os.makedirs()'''
# import os
# from turtle import mode 
# dir1 = "New"
# path1 = "C:/users/shabh/desktop"

# joiner = os.path.join(path1, dir1)


# os.mkdir(joiner) # creating directory Royal under desktop
# print ("Directory Created Successfully", dir1)


# dir2 = "Arin"
# path2 = "C:/users/shabh/desktop"
# mode = 0o666
# joiner = os.path.join(path2, dir2)


# os.mkdir(joiner,mode) # creating directory Royal under desktop
# print ("Directory Created Successfully", dir2)


#practice Question List of  os Module in a Python  using (os.cwd(),os.chdir(),os.mkdir())
'''
Ques 1: Create a folder named 'Python' in your Desktop and change the current working directory to that folder. 
'''