d="y"
while (d=="y"):
    a=int(input( "Enter 1st number:"))
    b=int(input("Enter 2nd number:"))
    print("""1.additon
        2.substraction
        3.divison
        4.multiplication""")
    c=int(input("which one do you wish run:"))
    if c==1:
        print(a+b)
    elif c==2:
        print(a-b)
    elif c==3:
        print(a/b)
    elif c==4:
        print(a*b)
    else:
        print("you faled the operation")
    d=(input("Do ypu want to continue? (n/y):"))
    
    
         



