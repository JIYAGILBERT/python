# a large block of code is divided into program is called functions
def addition():
    print("Enter 2 numbers")
    a=int(input("Enter a number:"))
    b=int(input("Enter a number:"))
    print(a+b)

def subtracton():
    print("Enter 2 numbers")
    a=int(input("Enter a number:"))
    b=int(input("Enter a number:"))
    print(a-b)


def division():
    print("Enter 2 numbers")
    a=int(input("Enter a number:"))
    b=int(input("Enter a number:"))
    print(a/b)


def multiplication():
    print("Enter 2 numbers")
    a=int(input("Enter a number:"))
    b=int(input("Enter a number:"))
    print(a*b)


print("1. addition 2. subtraction 3. division 4. multiplication")
c=int(input("Which one do you want to perform:"))

if c==1:
    addition()
elif c==2:
    subtracton()
elif c==3:
    division()
elif c==4:
    multiplication()
else:
    print("You faild the operation")    

    
