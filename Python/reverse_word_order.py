'''
Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

  My name is Michele
Then I would see the string:

  Michele is name My
shown back to me.
'''
'''
You can “split” or tear apart strings based on a given set of characters. For example:

  teststring = "this is a test"
  result = teststring.split("t")
And at the end, result will contain the list:

  ['', 'his is a ', 'es', '']
Instead of "t", you can write any character you want. If you do not include any character, it means “split on all whitespace”:

  teststring = "  this      has a lot    of   spaces and    tabs"
  result = testring.split()
Then result contains:

  ['this', 'has', 'a', 'lot', 'of', 'spaces', 'and', 'tabs']
Joining strings
You can also relatively easily “join” or “smush” strings together:

  listofstrings = ['a', 'b', 'c']
  result = "**".join(listofstrings)
Then result will contain the string:

  a**b**c
'''

def words_reverse():
	user_input = input("Enter Your String: ")
	result = user_input.split(" ")
	#reversing the string
	result = result[::-1]
	#joining spaces at each of the splits
	result = " ".join(result)
	print(result)

words_reverse()
