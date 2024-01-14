#Data_Types:-
'''
1. Integer(Int):-
ex: a=22
    b=-40
    c=33
print(type(a))
print(type(b))
o/p: <class 'int'>

2. Boolean:- True or False
ex: p=True
    q=False
    print(type(p),type(q))
o/p: <class 'bool'>

3. Float:- Numbers with decimal points.
ex: B= 0.5

4. Complex:
ex: K=3+2j
    print(type(K))
o/p:<class 'complex'

=> Type Conversion:
#If data loss is there then that conversion is known as "explicit conversion".
#If there is no data loss then it is known as "implicit conversion"


'''
a=22
b=4.0
c="Koppula Ganesh"
d=-22
print(type(a))
print(type(b))
print(type(a),type(b),type(c),type(d))
#type() function used to find the type of an object in the python.

p=True
q=False
print(type(p),type(q))

True==1
False==0
print(True==1)
print(False==0)
#Boolean

K=2+3j
print(type(K))
#complex=(real part)+(imaginary part)j

'''Type Conversion:- The process of converting the value of one data type (integer,
string, float, etc.) to another data type is called type conversion.
Python has two types of type conversion.
1. Implicit type conversion
2. Explicit type conversion '''

# for example lets convert int to float and vice versa.
A=2
print(float(A))
#in the ouput we got "2.0" which is a float.
#It is "the implicit conversion" there is no data loss in the above case.

B=3.5 #float (higher data type)
print(int(B))
'''
In the out put we got "3" which is an integer (lower data type). 
This conversion is known as 'the explicit conversion', 
where we lost the data from 3.5 to 3

'''