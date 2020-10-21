# oop concept
# oop is a process in which we treat everything as object
# object is an entity which has two parts 1)property 2)behaviour
# 1)property:-these are the specifications of objects
# 2)behaviour:-it determines actions which is an object performs
# to create an object we use class
# class: class is a template/blueprint using which we create objects
# class contains properties/datamembers and behaviour
# syntax:-
#         class Name:
#                 //datamembers
#                //behaviour
# to create an object we use the syntax-----Name()

# defing the class
# class IceCream:
#     type="cone"
#     flavour="Butterscotch"
#
#     def melt(self): //self key word reffers the current object
#         print("melting")
#
# creating object
# ice1=IceCream()
# print(ice1.type)
# print(ice1.flavour)
# ice1.melt()

# class Human:
#     gender="male"
#     age=24
#
#     def good(self):
#         print("Good hearted person")
#
#     def bad(self):
#         print("cruel person")
#
# person1=Human()
# person2=Human()
# # updating the values
# person1.age=26
# person2.age=35
# print(person1.gender)
# print(person1.age)
# print(person2.gender)
# print(person2.age)
# person1.good()
# person2.bad()



# class Human2:
#     gender="male"
#     age=24
#
#     def work(self):
#         print("working in IT company")
#
#     def time(self):
#         print("morning shift")
#
# person1=Human2()
# person2=Human2()
# print(person1.gender)
# print(person1.age)
# print(person2.gender)
# print(person2.age)
# person1.work()
# person2.time()


# class car:
#     name="contessa"
#     type="manual"
#     fuel="petrol"
#
#     def car1(self):
#         print("lover of hindustan contessa")
#     def car2(self):
#         print("just go audi")
#
#     def car3(self):
#         print("kia moters")
#
# veh1=car()
# veh2=car()
# veh3=car()
# veh2.name="audi"
# veh2.type="automatic"
# veh2.fuel="diesel"
# veh3.name="winder"
# veh3.type="manual"
# veh3.fuel="electric"
# print(veh1.name)
# print(veh1.type)
# print(veh1.fuel)
# print(veh2.name)
# print(veh2.type)
# print(veh2.fuel)
# print(veh3.name)
# print(veh3.type)
# print(veh3.fuel)
# veh1.car1()
# veh1.car2()
# veh1.car3()

#
# defing the class
# class IceCream:
#     type="cone"
#     flavour="Butterscotch"
#
#     def melt(self,newType): #//self key word reffers the current object
#         print("melting")
#         self.type=newType
#
# creating object
# ice1=IceCream()
# print(ice1.type)
# print(ice1.flavour)
# ice1.melt("cup")
# print(ice1.type)
#
# ice2=IceCream()
# print(ice2.type)
# print(ice2.flavour)
# ice1.melt("cup")
# print(ice2.type)



# defing the class
# class IceCream:
#     type="cone"
#     flavour="Butterscotch"
#
#     def melt(self,newType): #//self key word reffers the current object
#         print("melting")
#         self.type=newType
#     def __init__(self):
#         print("inside init method")
#
# # creating object
# ice1=IceCream()
# print(ice1.type)
# print(ice1.flavour)
# ice1.melt("cup")
# print(ice1.type)
#
# ice2=IceCream()
# print(ice2.type)
# print(ice2.flavour)
# ice2.melt("box")
# print(ice2.type)
#

#self:-self is used to acess the data numbers of the class inside a method
# self points to the current object
#constructor method:- every class has a default method called as constructor
# The name of the constructor __init__
#python automatically creates this constructor for every class
#Note: if the developers writes the unique method, python will not create the unique method
# while creating an object of a class, python calls the unique method of that class
#constructor is used for 2-purposes
#1) Object creation        2) Intialising the values for daa members/properties



# class IceCream:
#     type="cone"
#     flavour="butterscotch"
#
#     def melt(self,newType):
#         print("melting")
#         self.type=newType
#     def __init__(self,newFlavour):
#         print(" inside init method")
#         self.flavour=newFlavour
# ice1=IceCream("strawbwrry")
# print(ice1.flavour)
# ice2=IceCream("vanilla")
# print(ice2.flavour)

#  Constructor:-
# there are 2 types
#  1) 0-argument        2) parameterized constructor

#  0-argument constructor:-   These types of constructors does not accept any arguments
#   these constructs will have only one  defaultr argument called as  Self
#   Syntax:
#          def  __init__(self):
#                //statements

#  Parameterized arguments:-    these type of constructors which accepts arguments from the user
#  Syntax:
#          def  __init__(self):
#               //statements
# Note:    a clas have more than one init method
#          the last init method will be executed
#          the construct does not return anything
#          whenever python creates  a constructor it is 0- argument constructor


class Animal:
    name="horse"
    type="herbivours"

    def racing(self,newType):
        print("horse is ")
        self.type=newType

    def grass(self,newType):
        print("horse is ")
        self.type=newType

    def __init__(self,newName,newType):
        print("about animal ")
        self.name=newName
        self.type=newType

anl1=Animal("deer","vegitarian")
print(anl1.name)
print(anl1.type)
# anl1.racing("runnig")
# print(anl1.type)
anl2=Animal("tiger","non vegitarian")
print(anl2.name)
print(anl2.type)
# anl2.grass("eating")
# print(anl2.type)















