'''
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
'''
print("<-------------------------- Rock Paper Scissors -------------------------->")
#Enter the player names
user1 = input("\nEnter your Player 1 Name: ")
user2 = input("\nEnter your Player 2 Name: ")
#if this value is true we will exit the program by either none code or sys.exit()
quiting = False
#for entering the details of the players
def detail():
	u1 = input("\n%s, rock,paper, or scissors.\n> "% user1)
	u2 = input("\n%s, rock,paper, or scissors.\n> "% user2)
	#calling the game function to return either player 1 or player 2
	return game(u1,u2)

def game(u1, u2):
	if u1 == u2:
		return("Tie")
	if u1 == 'rock' and u2 == 'scissors':
		return("Player 1")
	elif u1 == 'scissors' and u2 == 'paper':
		return("Player 1")
	elif u1 == 'paper' and u2 == 'rock':
		return("Player 1")
	elif u2 == 'rock' and u1 == 'scissors':
		return("Player 2")
	elif u2 == 'scissors' and u1 == 'paper':
		return("Player 2")
	elif u2 == 'paper' and u1 == 'rock':
		return("Player 2")
	else:
		return("err")

		
while quiting != True:
	check = detail()
	if check == "Player 1":
		print("\n%s Wins!" % user1)
	elif check == "Player 2":
		print("\n%s Wins!" % user2)
	elif check == "Tie":
		print("\nThat's a Tie!")
	elif check == "err":
		print("\nInvalid Input")
		continue
	print("Wanna Play Again? (Y/N)")
	again = input("> ")
	if again == 'y' or again == 'Y':
		pass
	else:
		quiting = True
print("\nThank You For Playing!")
print("<-------------------------- Created By Abhi Saxena -------------------------->")