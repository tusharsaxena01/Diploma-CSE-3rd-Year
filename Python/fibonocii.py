'''
Write a program that asks the user how many Fibonacci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.
'''
count = int(input("Enter the length of series\n> "))
#indexing is starting at one because fibonocii index 0 value is 0
i=1
if count == 1:
	fib = [0]
elif count == 2:
	fib = [0,1]
elif count > 2:
	fib = [0,1]
	while i < (count-1):
		term = fib[i]+fib[i-1]
		fib.append(term)
		i+=1
print(fib)