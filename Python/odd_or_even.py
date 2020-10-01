#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
num = int(input("Enter any Number: "))
if num%2 == 0:
	print(num,"is Even!")
else:
	print(num,"is Odd!")