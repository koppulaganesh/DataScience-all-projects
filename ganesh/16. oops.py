'''
oops: oops is an object oriented programming language.
#oops concepts in python:-
1. class:
#Class is a blue print of an object. 
#It starts with the keyword "class"
#Class can be defined as a collection of objects. 
#It is a logical entity that has some specific attributes and methods.

#attributes: attributes define the properties of an object.
#methods: Method is a function that is associated with an object.
methods define the behaviour of an object.
'''
#class:
class Myclass():
    print("this is the class...")

    #output: this is the class...
    #class=keyword
    #Myclass=class name 
    #(class name should always start with captial letter)

class Myclass():
    print("this is class")
    def display(self):
        a=1
        b=2
        print(a,b)
obj=Myclass()
obj.display()
'''
output:-
this is class
1 2
'''

'''
2.object: Object is an entity that has state and behavior

'''

class Myclass():
    x=5
p1=Myclass() #p1 is an object name
print(p1.x)

class Python():
   a=2
   def output(self):
       print(self.a)
b=Python()
v=Python()
print(b.a)
print(b.output())



class Student:
    def name(self,name):
       self.name=name
    def getname(self):
       return self.name
student1=Student()
student1.name("GANESH")
print(student1.getname())

student2=Student()
student2.name("RAJESH")
print(student2.getname())

class Rectangle():
    def set_dimensions(self,width,height):
      self.width=width
      self.height=height
    def area(self):
       return self.width * self.height
    def perimeter(self):
       return 2*(self.height + self.width)
rectangle1=Rectangle()
rectangle1.set_dimensions(4,3)
print("The area of a rectangle is:",rectangle1.area())
print("The perimeter of a rectangle is:",rectangle1.perimeter())


class Car(): #class is keyword in the python and Car() is the class name always class name should start with capital leters.
    def set_car(self,name):
      self.name=name
    def get_car(self):
       return self.name
car1=Car()
car1.set_car("Car1: AUDI")
print(car1.get_car())
car2=Car()
car2.set_car("Car2: lamborghini")
print(car2.get_car())

a="virat kohli" #string length
print(len(a))
k=["virat","Dhoni"] #string length in list.
print(len(k))

class Myname():
    def set_name(self,name):
      self.name=name
    def get_name(self):
       return self.name
name1=Myname()
name1.set_name("Shiva")
print(name1.get_name())
name2=Myname()
name2.set_name("Adolf Hitler")
print(name2.get_name())
name3=Myname()
name3.set_name("Nelson Mandela")
print(name3.get_name())

#__int__() inbuilt function in python:
'''ex1: Create a class named Person, use the __init__() function to assign values for name and age'''
class Person():
   def __init__(self,name,age):
      self.name=name
      self.age=age
p1=Person("Name: Ganesh","Age:24")
print(p1.name)
print(p1.age)

'''ex2: Create a class name Car, use the __int__() function to assign values for color'''

class A():
   def __init__(self,name,age,height):
      self.name=name
      self.age=age
      self.height=height
a=A("Name: ganesh","age: 24","Height: 5.8ft")
print(a.name)
print(a.age)
print(a.height)


class Dog():
   def __init__(self,Breed,color):
      self.Breed=Breed  #Class attributes
      self.color=color
dog1=Dog("Dog1: pomeranian","Color: white")
print(dog1.Breed)
print(dog1.color)
dog1.Medal = "gold Medal"  #Instance attribute
print(dog1.Medal)
dog2=Dog("Dog2: German Shepherd","Color: Black")
print(dog2.Breed)
print(dog2.color)

'''
#Attributes:
1. class attribute
2. Instance attribute
'''
''''
#Access Modifiers:-
1.Public access modifers
2.Private access modifiers (we use two underscores __)
3.Protected access modifiers (we use one underscore _)
'''

class Employee():
   name="Ganesh"
   def changename (self):
      Employee.name="Raju"
employee1=Employee()
print(employee1.name)
employee1.changename()
print(employee1.name)




  





       
      
      



    
    







       
  