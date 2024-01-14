'''
Access specifiers: 
1. Public
2. protected #we use sing underscore for protected
3. private #we use double underscore for private
'''
#1. Public: here we are accessing the class and methods even outside the class so it is called as public.
class Student():
    def __init__(self,name):
        self.name=name  #public instance variable
    def display(self):
        print("Hello my name is Ganesh...!")
s1=Student("Ganesh")
print(s1.name)
s1.display()    
#here we are accessing the class and methods even outside the class so it is called as public.

#2. Protected: we can access within the class and well as derived class.
class Student():
    def __init__(self,name,rollno):
        self.name=name  #public instance variable
        self._rollno=rollno #protected instance variable
    def display(self):
        print("Hello my name is janine...!")
s1=Student("janine",24)
print(s1.name)
s1.display() 
print(s1._rollno) #here we are accessing the protected.

#3. Private: we cannot access private attribute outside of the class.
# If you try so it will give you an error.
class Student():
    def __init__(self,name,age,rollno):
        self.name=name  #public instance variable
        self._rollno=rollno #protected instance variable
        self.__age=age
    def display(self):
        print("Hello my name is RGV...!")
s1=Student("RGV",24,1034)
print(s1.name)
s1.display() 
print(s1._rollno)
print(s1.__age) 
#here we get an error because we cannot access the private attribute.
# AttributeError: 'Student' object has no attribute '__age'


