'''Print ascii value of the given value using python'''
#using two functions ord to convert into a number and chr to convert back into number format
#using exception handling to create a program that is short in length
i = input("Enter the character\n> ")
try:
	b = chr(int(i))
	print(b)
except:
	a = ord(i)
	print(a)

print("Thank You for using...\n\tMade by Tushar Saxena")
