#printing the name
def printname(name, number):
    print("The name is: ",name)
    print("The number is: ",number)

    if name=="pranith":
        print("Hello, ",name)


printname("pranith", 57)

#Checking for the github

#checking for the prime number

def findprime(num):
    if num>1:
        for i in range(2,num-1):
            if num%i==0:
                print("The number is not prime")
                break;
            else:
                print("The number is prime")
                break;
    else:
        print("The number is prime")


findprime(13)
