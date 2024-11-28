# OBJECT ORIENTED PROGRAMMING [OOP]
 # -  
# class = user defined data type
# method = class 

# class car:
#     def __init__(self,name,color):
#         self.name=name
#         self.color=color
#     def disp(self):
#         print("name",self.name)
#         print("color",self.color)
#         # print("Hello world")
# obj1=car("swift","red")
# obj1.disp()

class Bank:
    def __init__(self,balance):
        self.balance=balance
    def deposit(self):
        a=int(input("Enter the amount:"))
        self.balance=self.balance+a
        print("cash deposited")
    
    def withdrawl(self):
        b=int(input("How much you want to withdraw:"))
        if b<=self.balance:
            print("Amount debited")
            self.balance=-b
        else:
            print("insufficent balance")  
    
    def check_balance(self):
        print(self.balance)
        
    
   
# obj1=Bank(0)
# d="y"
# while(d=="y"):      
#     print("1. deposit 2.withdrawl 3.check balance 4.exit")
#     c=int(input("Which one do you want to run:"))
#     if c==1:
#         obj1.deposit()
#     elif c==2:
#         obj1.withdrawl()
#     elif c==3:
#         obj1.check_balance()
#     elif c==4:
#         print("exit.....")
#     else :
#         print("Thank you!")
    # d=(input("Do ypu want to continue? (n/y):"))  












