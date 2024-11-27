# a large block of code is divided into program is called functions
# def addition():
#     print("Enter 2 numbers")
#     a=int(input("Enter a number:"))
#     b=int(input("Enter a number:"))
#     print(a+b)

# def subtracton():
#     print("Enter 2 numbers")
#     a=int(input("Enter a number:"))
#     b=int(input("Enter a number:"))
#     print(a-b)


# def division():
#     print("Enter 2 numbers")
#     a=int(input("Enter a number:"))
#     b=int(input("Enter a number:"))
#     print(a/b)


# def multiplication():
#     print("Enter 2 numbers")
#     a=int(input("Enter a number:"))
#     b=int(input("Enter a number:"))
#     print(a*b)


# print("1. addition 2. subtraction 3. division 4. multiplication")
# c=int(input("Which one do you want to perform:"))

# if c==1:
#     addition()
# elif c==2:
#     subtracton()
# elif c==3:
#     division()
# elif c==4:
#     multiplication()
# else:
#     print("You faild the operation")    

# def add(x,y):
#     print(x+y)
# a=int(input("Enter a number:"))
# b=int(input("enter a number:"))
# add(a,b)





############### dctionary ill cheyyan###########
###########>>>>>> arbitrary arguments >>>>>>>>>>
# def addition(**x):
#     print(x["a"]+x["b"])
# addition(a=5,b=6)



          ################ using tupple #################
# def add(*x):
#     print(x[0]+x[1])
# a=int(input("Enter a number:"))
# b=int(input("enter a number:"))
# add(a,b)

# >>>>>>>>>> Key word arguments <<<<<<<<<<<<<

# def add(x=5):
#     print(x)
# add(10)


################ return statement ##################

     # >>>>>>>>>>>> add cheyyum bt print avvvilla
# def add(a,b):
#     return a+b
# add(5,4)

# >>>>>>>>>>>> add cheyyum >>>>>
# def add(a,b):
#     return a+b
# print(add(5,4))


# 1)Q. write a program that accepts a list using function and returns two list one containing odd and one containing even numbers.


# def odd_even(numbers):
#     e=[]
#     o=[]
    
#     for num in numbers:
#         if num % 2 == 0:
#             e.append(num)
#         else:
#             o.append(num)
    
#     return e, o

# input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even, odd = separate_odd_even(input_list)

# print("Even numbers:", even)
# print("Odd numbers:", odd)

odd=[]
even=[]
def odd_even(number):
  
    for number in list1:
        if number % 2==0:
            odd.append(number)
        else: 
            even.append(number)
    return odd,even
list1=[1,2,3,4,5,6,7,8,9,10]
odd_even(list1)
print("Even number:",odd)
print("Odd number:",even)
        


    


















