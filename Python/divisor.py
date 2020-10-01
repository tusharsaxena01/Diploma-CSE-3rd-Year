#Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
num = int(input("Enter any number: "))
divisors = []
for i in range(1,num+1):
	if num % i == 0:
		divisors.append(i)


#another way
'''
list_range = list(range(1,num+1))
for i in list_range:
	if num % i == 0:
		divisors.append(i)
'''
print(divisors)