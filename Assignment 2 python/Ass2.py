# Assignment 2.1 = Remove all occurance of an element from a list

li = [1,3,5,2,1,5,1,7,1,8]
val = 1
li = [value for value in li if value != val]
print(li)
