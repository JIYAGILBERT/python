# single inheritance #
# class Vehicle:
#     def work():
#         print("move")

# class Car(Vehicle):
#     def wheels():
#         print("Four wheler")
# obj1=Car
# obj1.work()


#  multi-level inheritance #
# class Vehicle:
#     def work():
#         print("move")

# class Car(Vehicle):
#     def wheels():
#         print("Four wheler")

# class Swift(Car):
#     def color():
#         print("black")
    

# obj1=Swift
# obj1.work()
# obj1.wheels()
# obj1.color()

# class Two_wheeler:
#     def work():
#         print("move")

# class Four_wheeler():
#     def wheels():
#         print("Four wheler")

# class Three_wheeler(Two_wheeler,Four_wheeler):
#     def color():
#         print("black")
    

# obj1=Three_wheeler
# obj1.work()
# obj1.wheels()
# obj1.color()

###############hierarchial inheritanc ###############
# class Human:
#     def child():
#         print("girl/boy")

# class Girl(Human):
#     def child1():
#         print("Girl")

# class Boy(Human):
#     def child2():
#         print("boy")
    

# obj1=Girl
# obj2=Boy
# obj1.child1()
# obj2.child2()

class A1:
    def a1():
        print("hey A1")
    
class B1(A1):
    def b1():
        print("hey B1")
        
class C1(B1):
    def c1():
        print("hey c1")
        
class D1(B1):
    def d1():
        print("hey d1")
        
class E1(D1):
    def e1():
        print("hey e1")
    
class F1(C1,D1):
    def f1():
        print("Hey f1")

obj1=F1
obj2=E1

obj1.a1()
obj1.b1()
obj1.c1()
obj1.d1()
obj1.f1()

obj2.e1()        
















