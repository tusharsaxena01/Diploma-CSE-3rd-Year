#Roll a random face of the dice
import random

def roll_dice():
	dice_face = random.randint(1,7)
	print(dice_face)

print("\nType EXIT at any prompt to Exit...\n")

while True:
	choice = input("\nRoll a dice?(Y/N)\n> ")
	if choice == "EXIT" or choice == "exit":
		break
	if choice == 'Y' or choice == 'y':
		roll_dice()
	elif choice == 'N' or choice == 'n':
		break
	else:
		print("\nPlease Enter valid Input!\n")
	continue