#Tuple: 
'''
1.we use tupple when we have constant data.
2.Tupple is immutable(we cannot modify the data)
3.It allows different data types.
4.It allows indexing and slicing.
5.It allows duplicates.
6.No methods in tuple, but we can use builtin.

'''
a=(1,2,3,4,5.6,"ganeshkoppula",True)
print(a[-2]) #You can access tuple items by referring to the index number, inside square brackets.
print(len(a)) #no. of elements = len
print(a[0:4]) #The search will start at index 2 (included) and end at index 5 (not included).

#Concatenation: To add to tuples...
t1=(1,2,3,4,5)
t2=(6,7,8,9,0)
print(t1+t2)
#o/p:(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

#repetation: 
a1=(1,2)
print(a1*5)
#o/p: (1, 2, 1, 2, 1, 2, 1, 2, 1, 2)

a=(1,2,3,4,5,6,7,8,9,0)
print(max(a)) #maximum element
print(min(a)) #minimum element
print(sum(a)) #addition of elements
print(len(a)) #To determine how many items a tuple has, use the len() function

#tuple with one item:
#To create a tuple with only one item, you have to add a comma after the item, 
# otherwise Python will not recognize it as a tuple.
b=("ganesh",)
print(type(b)) #<class 'tuple'>

#Using the tuple() method to make a tuple:
c=tuple(("ganesh","komal","suresh")) # note the double round-brackets
print(c)
print(type(c))

#membership operations:
d=(32,34,5,6,7,8,9)
print(32 in d) #True
print(21 not in d) #True
print(1 in d) #False
print(9 in d) #True

d1=(1,2,3,4,5,6,7)
d2=(23,34,56,78,90)
print(d1 is d2) #False
print(d1 is not d2) #True

d3=(1,2,3,4,5,6,7,8,9,0)
d4=(1,2,3,4,5,6,7,8,9,0)
print(d3 is d4) #True
print(d3 is not d4) #False



a=(1,2,3,4,5.6,"ganeshkoppula",True)
print(type(a))
 
a=()
print(type(a))

x=(1,2,3,4,5,6)
print(x[0])
print(x[1])
print(x[2])
print(x[3])
print(x[4])
print(x[5])
# print(x[6])
# print(x[1.0])

y=("ganesh",1,3.0,[123,23,4])
print(y[3][0])

z=(1,2,3,4,5,6)
print(z[-1])
print(z[-2])
print(z[-3])
print(z[-4])
print(z[-5])
print(z[-6])

v=('p','q','r','s')
print(v[0:4])
print(v[:])

n=1,2,3,4,5 #no parentheses
print(type(n))

n=1,
print(type(n))

p=("a",) #with comma is a tuple
print(type(p))

p=("a") #without comma is a string 
print(type(p))

x=(1,2,3,4,5,6)
print(1 in x)
print(7 not in x)
print(0 in x)

b=("ganesh","Janine")
x,y=b
print(x)
print(y)