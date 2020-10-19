#PracticePython.org
#Create a prgm that asks the user to enter thier name and their age. print out a message addressed to them that tells them the year they will turn 100 years old
name = input("Enter your name: ")
age = int(input("Enter your age: "))
current_year = int(input("Enter Current Year: "))
yr = str((current_year - age)+100)
print("\nHey "+name+"!"+"\nYour Current age is ",age,"\nYou'll Turn 100 in the next "+yr)
