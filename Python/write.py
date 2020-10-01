'''
Write a program that creates two file
first file should contain all prime numbers upto a given limit
and another file should contain all the numbers in that limit

#the files are to be used in 'file_overlapping' program
'''
file = open('primenumbers.txt','a')
for i in range(1,10):
	c=0
	for n in range (2,i):
		if i%n==0:
			c+=1
	if c==0:	
		file.write("%i\n"%i)

file.close()

file = open('happynumbers.txt','a')
for i in range (1,10):
	file.write("%i\n"%i)

file.close()