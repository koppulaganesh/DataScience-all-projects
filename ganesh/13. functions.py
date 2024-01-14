#13.Functions: 
'''
1.In Python a function is defined using the "def" keyword.
2.Function is nothing but a "block of code"(a set of instruction to perform code).
3.By importing the code we can reuse it.

'''
def add(a,b): #function definition
    print(a+b) #function body
add(1,2) #fuction call
'''
def=key word
add=function Name
(a,b)=parameters
print(a+b)=function body
(1,2)=arguments
add(1,2)=function call
'''

#Nested function(function within a function):
def outer():
    print("outer")
    def inner():
        print("inner")
    inner()
outer()
'''
   o/p: outer
        inner
'''
def func():
    print("hello my friend!!")
func()

def mango():
    print("fruit")
mango()

def add(a,b,c,d):
    print("this is addidion",a+b+c+d)
add(1,2,3,4) #this is addition 10

#arbitary parameters/arguments:
def my_function(*a):
    print("this is function",a)
my_function(1,2,3,4) #(1,2,3,4) tuple

#Keyword arguments:-
def func(**a):
    print("this is where we stand",a)
func(a=1,b=2,c=3) #{'a': 1, 'b': 2, 'c': 3} dict

#importing the code to reuse the mathematical operations:
def add(a,b):
    print(a+b)
add(4,5)

def sub(a,b):
    print(a-b)
sub(10,5)

