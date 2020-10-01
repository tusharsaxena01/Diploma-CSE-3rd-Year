'''
Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
'''
#Sets - In mathematics, a set is a collection of elements where no element is repeated. This becomes useful because if you know your data is stored in a set, you are guaranteed to have unique elements.
a=[1,2,3,4,4,3,2,1]
#using sets
def modify_v1(derived_list):
	return set(derived_list)

#using loop
def modify_v2():
	b=[]
	for i in a:
		if i not in b:
			b.append(i)
	return b


print(modify_v1(a))
print(modify_v2())