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


#Factorial to start of with

def factorial_calculation(x):
    if x==1:
        return 1
    else:
        return (x*factorial_calculation(x-1))

num=5
print("The factorial of ",num," is: ",factorial_calculation(num))

i = 2
while(i < 100):
   j = 2
   while(j <= (i/j)):
      if not(i%j): break
      j = j + 1
   if (j > i/j) : print i, " is prime"
   i = i + 1

print "Good bye!"

