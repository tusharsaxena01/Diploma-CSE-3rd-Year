#Ask the user for a string and print out whether this string is a palindrome or not.
s1 = str(input("Enter the String: "))
#reverse
s2 = str(s1[::-1])
if s1 == s2:
	print("Palindrome!")
else:
	print("Not Palindrome!")