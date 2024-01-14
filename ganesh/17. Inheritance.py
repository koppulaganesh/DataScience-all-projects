'''Inheritance:-
1. single inheritance
2. Multilevel inheritance
3. Multiple inheritance
4. Hierarchial inheritance
'''
#1. Single Inheritance:-
class Father():
    def outputf(self):
        print("This is your father...")
class Son(Father):
    def outputs(self):
        print("I'm your son dad...")
a=Son()
print(a.outputs())

class Playstore():
    def apps(self):
        print("all apps are registered with google")
class Gpay(Playstore):
    def app(self):
        print("Google Pay")
b=Gpay()
b.apps()
b.app()


class Mettu_Ramulu():     #parent class or base class
    def father(self):
        print("I'm a railway employee")
class Ganesh(Mettu_Ramulu):  #child class or derived class
    def son(self):
        print("I'm an unemployee")
k= Ganesh()
k.father()  #parent method
k.son() #child method


#2. multilevel Inheritance:-

class Grandfather():
    def outputgf(self):
        print("I'm your grandfather")
class Father(Grandfather):
    def outputf(self):
        print("I'm your father")
class Son(Father):
    def outputs(self):
        print("I'm your son")
s=Son()
s.outputgf()
s.outputf()
s.outputs()

#3. multiple inheritance:

class Mother():
    def outputm(self):
        print("Rajamani")
class Father():
    def outputf(self):
        print("Mettu Ramulu")
class Son(Father, Mother):
    def outputs(self):
        print("Ganesh")
d=Son()
d.outputm()
d.outputf()
d.outputs()

#4. Hierarchial inheritance:

class Parent():
    def outputp(self):
        print("Parent")
class Child1(Parent):
    def outputc1(self):
        print("Child1")
class Child2(Parent):
    def outputc2(self):
        print("child2")
k=Child1()
p=Child2()
k.outputc1()
k.outputp()
p.outputc2()
p.outputp()