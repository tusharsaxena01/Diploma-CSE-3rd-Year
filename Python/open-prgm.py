#Creating a user friendly program to open desired file using desired program
'''Denoting the procedure through numbering'''
#1
#importing different modules for the program
import os
import subprocess as sp
import banner_generator as bg #remove if you don't have my banner generator
#13
#now calling the function fileChoose from dirChoose and retaining the value argument directory
def fileChoose(directory):
	#14
	#asking if program should list the files present in that directory
	ch = input("\nList Files?(Y/N)\n> ")
	#15
	#files variable would hold the list of the files in that directory
	files = os.listdir(directory)
	#16-1
	#if value of varable ch is 'Y','y',or 'Yy'
	if ch in 'Yy':
		#17-1
		#for a variable i whose value would gradually increase from 0 to length of files-1
		for i in range (0,len(files)):
			#18-1
			#while the condition is true it would list out the elements of the list variable files and i is index here
			print(files[i])
		#18-1
		#creating a variable fileName with the value blank
		fileName=''
		#19-1
		#while the filename is not present in the list files then this section would be executed
		while fileName not in files:
			fileName = input("Enter File Name (With Extension):\n> ")
			#20-1
			#if the input filename is present in the files list then this code would be executed
			if fileName in files:
				#21-1-1
				#return the filename to dirChoose functions and then it would return the corresponding to the main calling function with is #3
				return fileName
			#21-1-2
			#if the file is not found in the directory then
			else:
				print("File Not Found!\n")
				#22-1
				#again sending the interpreter to the check of the condition of the loop
				continue
	#16-2
	#if the above condition is not true then this would check if the value of ch is 'n' , 'N' or 'Nn'
	elif ch in 'Nn':
		#17-2
		#creating a variable fileName with the value blank
		fileName = ''
		#18-2
		#until the filename is not present in the list files this statement would be executed
		while fileName not in files:
			fileName = input("\nEnter File Name (With Extension):\n> ")
			#19-2
			#if the filename is now present in list files
			if fileName in files:
				#20-2-1
				#returning the file name to dirChoose and then to the filename variable calling them at #3
				return fileName
			else:
				print("File Not Found!\n")
				#20-2-2
				#again sending the interpreter to the checking the condition of the loop
				continue
	#16-3
	#if the file is not found in the list files
	else:
		print("\nError Occurred!\nExiting...\n")
		#17-3
		#returning 'file not found' which would work as a switch to exit from the program
		return "File Not Found" #if return value is error then no other operation performed
#4
def dirChoose():
	#5
	#if the chnge value is assigned to make the condition true then only the loop would be executed
	chnge = 'Y'
	#6
	#if value of variable is among 'Yy', the loop would be executed
	while chnge in 'Yy':
		print("\nCurrent Working Directory:\n")
		#7
		#calling the method getcwd() of os module to get the "Current Working Directory"
		print(os.getcwd())
		#8
		#taking input into the variable chnge
		chnge = input("\nChange Directory? (Y/N):\n> ")
		#9
		#if value input is among 'Yy' then this operation would be performed
		if chnge in 'yY':
			directory = input("\nEnter the full path of the directory you want to visit (is Case Sensitive):\n> ")
			#10-1
			#passing the directory to chdir method of os module to "Change Directory"
			os.chdir(directory)
			#11-1
			#after changing the current directory once again it is prompted if he wants to change directory
			continue
		#10-2
		#if value of chnge is not "y" or 'Y' then it checks the second condition if the value is 'N' or 'n' or 'Nn'
		elif chnge in 'Nn':
			#11-2
			#if user does not want to change the directory then we would change the variable directory value to the current directory
			directory = os.getcwd()
			#12
			#returns the value that would be returned by fileChoose functions and passing the argument directory into the function
			return fileChoose(directory)
		#10-3
		#if both above conditions are false then this condition is implemented
		else:
			print("\nPlease Enter Valid Option!")
			#setting the value of variable chnge again to Y inorder to get the loop working again and prompting again for the number 6
			chnge = 'Y'
#25
#here the function is created inorder to choose among the program to open the file
def programChoose():
	print("\nChoose Program:")
	#26
	#creating a list with elements of the attributes accepted by the subprocess module
	#at this time I only know about one of the attribute which is notepad so here is the list with the elements which would be passed to create the execution of the desired file into this program
	progm = ['notepad'] #can add elements later
	#27
	#for any variable i whose value would gradually increase from 0 to length of the list progm-1
	for i in range(0,len(progm)):
		#28
		#using formatting in the print method which can be found online
		print("%i. %s"%(i, progm[i])) #basic syntax is to use the '%' sign and the correspoding letter to denote the data type (inherited into python From C language) and then add %(var1,var2)
	#29
	#after list various programs the user has to give input according to the index in the variable ch
	ch = int(input("\n> "))
	#30-1
	#if the value of variable ch is less than length of list progm this would execute
	#concept is becuse if the length of any list is 4 then it's indexing would go until length-1 #Simple Array Definition
	if ch < len(progm):
		#31-1
		#inorder to pass the attribute to the subprocess module this formatting is neccessary. here we are adding '.exe' at the end of the element in list progm
		programName = progm[ch]+".exe"
		#32-1
		#now returning the value to the calling variable
		return programName
	#30-2
	else:
		print("\nProgram Not Found!\nExiting...\n")
		#31-2
		#if the program is not found then this statement would be returned to the calling variable to exit the program
		return "\nProgram Not Found"
#2
#Generating Banner using my banner generator file
bg.generate("Welcome!") #remove if you don't have my banner generator
print("Open Files using Notepad and other Programs(in later programs)")
#3
#calling the function dirChoose to return into the variable fileName
fileName = dirChoose()
#23
#if return value is file not found then perform this banner generating operation
if fileName == "File Not Found":
	#24-1
	#if the return statement is file not found then execute this line and exit
	bg.generate("See You Later...\n")	#remove if you don't have my banner generator
else:
	#24-2
	#the value of the variable programName would be the value which is returned by the function programChoose
	programName = programChoose()
	#33-1
	#if return value is program not found then execute these lines of code and exit the program
	if programName == "Program Not Found":
		#34-1
		#generating a banner from my banner generator file
		bg.generate("See You Later...\n")	#remove if you don't have my banner generator
	#33-2
	#if the return value is other than program not found then this would be executed
	else:
		#34-2
		#calling the module subprocess which is imported as sp and its method Popen which would open the desired program passed to it
		#it needs two attributes first, program name. and second, then file to be opened
		sp.Popen([programName, fileName])
		#35
		#Now just generating the banner for a closing message and credit
		bg.generate("Thank You For Using")	#remove if you don't have my banner generator
		print("\t\t\t\t\t\t-Made By Tushar Saxena")