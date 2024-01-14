''' #Python:-
1.python is integrated,object oriented and high level language.
2.python is a case sensitive in nature.
3.Guido Van Russom was the author of python programming language in the year of 1991.
For example: print() is the right function and Print() is the wrong wrong function used in the python.
Topic to be learned:
1.How to run in Visual studio.
2.Simple Hello world! execution.
3.Length
4.id method to find the memory address.
'''
print("Hello world!") #o/p: Hello world!
a=12
k=10
print(a+k) #o/p: 22

x=10
y=12
print(x+y) #o/p: 22

#for loop:-
a=[1,2,3,4,5]
for i in a:
    print(i)
#for loop: the loop of mentioned elements only.

m=["ganesh","ramesh","suresh"]
print(m) #o/p: ['ganesh', 'ramesh', 'suresh']
print(id(m)) #id method is used to find the memory address.
m[0]="kamesh" #0 is the index of "ganesh" which we wanna replace with "kamesh".
print(m)  #o/p: ['kamesh', 'ramesh', 'suresh']
#note: strings are immutable. That's why we used list to modify in the above....
print(id(m)) #o/p: 1998728221952
print(len(m)) #o/p: 3
#mutable: we can modify the elements as per our requirement.

g="john wick"
print(len(g)) #o/p: 9 (we have 9 elements in the string including space.)

h="ganesh koppula"
print(id(h)) #o/p: 1998728078704
print(len(h)) #o/p: 14
#len() is used to find the length or number of elements in an object.

print("Ganesh \n laptop")
print('ganesh\nkoppula') # \n is used for new line...

print(r"rawstring\n")    # raw string

