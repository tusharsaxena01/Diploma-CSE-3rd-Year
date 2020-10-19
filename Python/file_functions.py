#Write a program to write into an extrernal file using python
'''
Also it got some code that would explain how to open file in Read Only and Write Mode, also to add content into as file.
'''
#if the file doesn't exist it would create a new file into the current directory
file1= open('NewFile.txt','w') #here w means i'm opening this file in write mode
file1.write("Hey! Writing using Python")
file1.close()

#Add content to the file

#file1 = open('NewFile.txt','r+') #opening the file in read and write mode but it would overwrite the file contents
file1 = open('NewFile.txt','a') #Opening the file to append
file1.write("\nContent Added Using append")
file1.close()

#Opening a file in read only mode

file1 = open('NewFile.txt','r')
print(file1.read())
file1.close()

#This code reads the file line by line if used with a loop otherwise it shows only first line of the file

'''
print(file1.readline())
'''
