# take input for a list and sort a list in decending order 

li=[int(i) for i in input('enter values: ').split()]
li.sort(reverse=True)
print(li)