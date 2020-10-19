'''
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
'''
#This is thhe random module which would generate random number between any range (if given), from a list that so given times or till infinity
import random
#range in the random module includes the numbers given for the range
num = random.randint(1,9)
chances = 0
exit = False



print("\n<------------------------------ Guessing Game ------------------------------->")
while not(exit):
	print("\nEnter exit anytime to exit ;)")
	user_input = input("\nEnter the guess (1-9)\n> ")
	chances+=1
	if user_input in "exitExitEXIT":
		print("\nThank You For Playing!")
		print("\n<-------------------------- Created By Abhi Saxena -------------------------->")
		exit = True
		continue
	elif int(user_input) == num:
		print("You Guessed it Right!")
		print("Chances taken",chances)
		print("\nThank You For Playing!")
		print("\n<-------------------------- Created By Abhi Saxena -------------------------->")
		exit=True
		continue
	elif int(user_input) < num:
		print("Your Guess was Lower")
	elif int(user_input) > num:
		print("Your Guess was Higher")
	else:
		print("Invalid Input!")
