#Inheritance example 1 
# class Animal:
#     def speak(self):
#         print("Speaking")
# class Dog(Animal):
#     def bark(self):
#         print("barking")
# class Cat(Animal):
#     def meow(self):
#         print("meowing")
# dog = Dog()
# dog.speak()
# cat = Cat()
# cat.meow()

########
#2 
# class Animal:  
#     def speak(self):  
#         print("Animal Speaking")  
# class Dog(Animal):  
#     def bark(self):  
#         print("dog barking")  
# d = Dog()  
# d.speak()

###########
#3 
# class Calculation1:  
#     def Sum(self,a,b):  
#         return a+b;  
# class Calculation2:  
#     def Mul(self,a,b):  
#         return a*b;  
# class all(Calculation1,Calculation2):  
#     def Div(self,a,b):  
#         return a/b;  
# d = all() 
# print(d.Sum(8, 5))
# print(d.Mul(7, 4))
# print(d.Div(9, 3))

###############
# poly
# class Bird:
#     def intro(self):
#         print("There are many types of birds.")

#     def flight(self):
#         print("Most of the birds can fly but some cannot.")
# class sparrow(Bird):
#     def flight(self):
#         print("Sparrows can fly.")

# class ostrich(Bird):
#     def flight(self):
#         print("Ostriches cannot fly.")

# obj_bird = Bird()
# obj_bird.intro()
# obj_bird.flight()

# obj_spr = sparrow()
# obj_spr.intro()
# obj_spr.flight()

# obj_ost = ostrich()
# obj_ost.intro()
# obj_ost.flight()

#########
#encp
# class name :
#     def __init__(self):
#         self.name = "soham"
#         self.number = 9428354814
# class derived(name):
#     def __init__(self):
#         name.__init__(self)
#         print(self.number)
# obj = derived()
# # print(obj.name)
# # print(obj.__number)

##########
#abs    
# from abc import ABC  
# class Animal(ABC):
#     def speak(self):
#         pass
# class Dog(Animal):
#     def bark(self):
#         print("barking")
# class Cat(Animal):
#     def meow(self):
#         print("meowing")
# dog = Dog()
# dog.bark()
# cat = Cat()
# cat.meow()   

