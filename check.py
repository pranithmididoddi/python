import numpy as np

# a=np.array([1,2,3])
# print type(a)
# print a.shape

b=np.array([[1,2,3],[4,5,6]])
print b.shape
print b[1,2]

#List

mylist=[3,1,2]
print type(mylist)

myset=set([3,2,1])
myset.add(3)
print type(myset)
print myset

# Loops in python

count = 0
while (count < 9):
    print ("The count is:", count)
    count = count + 1

print("This is while")

for letter in 'pranith':
    print ("Current letter is: ", letter)

fruits = ["banana", "apple", "mango"]
for fruit in fruits:
    print("the fruit is: ", fruit)

