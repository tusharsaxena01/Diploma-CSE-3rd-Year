#Flip a coin

import random

def flip():
	side = random.randint(0,3)
	if side == 0:
		print("Heads!")
		return
	elif side == 1:
		print("Tails!")
		return
	elif side == 2:
		print("Woops! It was a Mid Way...")
		return

def greet():
	print("===Thank You For Playing===\n\t-Abhi Saxena")

ch = input("Flip a Coin? (Y/N/Exit)\n> ")
while ch not in "exitEXIT":
	if ch =="Y" or ch == "y":
		flip()
		ch = input("Flip a Coin? (Y/N/Exit)\n> ")
	elif ch =="N" or ch == "n":
		break
	else:
		print("invalid Input!\nTry Again...")
		ch = input("Flip a Coin? (Y/N/Exit)\n> ")
greet()