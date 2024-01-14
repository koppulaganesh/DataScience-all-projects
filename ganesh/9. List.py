'''List:--
#square brackets[] are used for the list. 
#we can store different elements in the list.
#it allows duplicates in the same list.
#it is mutable(we can change the values in the list)
#it also allow indexing.
'''
k=[1,2,3,4,'ganesh',8.90]
print(k[4]) #o/p: ganesh
print(k[-1]) #o/p: 8.9
print(type(k)) #o/p: <class 'list'>
print(k[0:5:2]) #o/p: [1,3,'ganesh'] #this is known as slicing.

#append(): we can add the element in the last of the list.
h=["komal sigchi",1.23,34,1234,2,3,4,5,6,7,8,9,0]
h.append("ganesh")
print(h)
# o/p:['komal sigchi', 1.23, 34, 1234, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'ganesh']

#extend(): we can add the bulk data in the list.
p=["ganesh","sahith",'ramulu','rajamani']
p.extend([1,2,3,4])
print(p)
#o/p: ['ganesh', 'sahith', 'ramulu', 'rajamani', 1, 2, 3, 4]

#count()
l=[1,2,3,4.5,4.6,5,7,8,1,1,1]
print(l.count(1)) # 1 is repeated for 4 times.

j=[1,2,3,4,5,"ganesh","ganesh","ganesh"]
print(j.count("ganesh")) #"ganesh" repeated for 3 times.
#remove: we can remove the element mentioned
j.remove(2)
print(j)
#o/p: [1, 3, 4, 5, 'ganesh', 'ganesh', 'ganesh']

#pop: pop is also used to remove the element by mentioning the index of the elemnt.
q=[1,2,3,4,5,6,7,8,9,0]
q.pop(2)
print(q) #3 got removed in the above list based on the index given.

#index: we can find the index by giving the element in the list.
o=[1,2,3,4,5,6,7,8,9,0]
o.index(0)
print(o.index(0)) #9 is the o/p


f=[1,2,3,4,5,6,78,34,4,5,6,"ganesh","ramulu"]
f.insert(0,"xyzpqr")
print(f)
#o/p: ['xyzpqr', 1, 2, 3, 4, 5, 6, 78, 34, 4, 5, 6, 'ganesh', 'ramulu']

L1=[10,20,30,40]
L1[1]=25 # just wanted to replace 20 with 25
print(L1) #o/p:[10, 25, 30, 40]
print(L1[0]) #10

#for loop for list
k=[1,2,3,4,5,6,7,89,'ganesh']
for i in k:
    print(i)

x=[1,2,3,4,5] #a list of 5 integers
y=["Ganesh","Ramesh","suresh","Rajesh"] #a list of strings
z=["Raju",2,2.76,[10,20]] #a list within another list is "nested"
p=[] #a list contains no elements is known as empty list.

numbers=[2,4,6,8,10,12,14,16,18]
numbers[0]=3
print(numbers)
print(numbers[-1])

rollno=[20,30,40,50,60,70,80,90]
print(rollno[-1]) #backward or negative indexing

rollno=[20,30,40,50,60,70,80,90]
print(rollno[0])  #forward or positive indexing

Actors=["Prabhas","Samantha","Trisha"]
print("Trisha" in Actors)
print("Salman" in Actors)

z=["Raju",2,2.76,[10,20]]
print(len(z))

p=[1,2,3,4,5]
q=[6,7,8,9,10]
print(p+q) #concatenation

r=[1]
print(r*8)

n=[1,2,3,4,5,6,7,8,9,10]
print(n[0:4])
print(n[:])
print(n[:9])
print(n[0:])

k=[3,6,9,12,15,18,21,24,27]
k[0:5]=[1,2,3,4,5]
print(k)

h=[1,2,3,4,5,6,7,8,9,10]
print(h[0:9:2])  #slicing method

name= ["ganesh","rajesh","suresh","ramesh","kamesh"]
name.append("mallesh")   #append method
print(name)

p=[9,8,7,6,5]
p.sort()  #sort method
print(p)

o=["ganesh","ramesh"]
k=[1,2,3,4]
o.extend(k)    #extend method
print(o)

l=[4,8,12,16,20,24,28]
l.remove(20) #remove method
print(l)

j=[5,10,15,20,25]
j.pop() #pop/remove method 
print(j)

f=[7,14,21,28,35,42,49]
f.pop(-2) #pop method with index
print(f)

d=[6,12,18,24,30,36]
d.insert(0,42)
print(d)

flowers=["jasmine","lotus","sun flower","rose"]
print(flowers.index("jasmine"))

numbers=[1,2,3,2,1,1,1,2,2,3,]
numbers.count(1)
print(numbers.count(1))

x=[]
print(type(x))

r=[1,2,3,4,5,6,7,8,9,10]
print(max(r))
print(min(r))
print(len(r))
print(sum(r))

x="Lenovo"
print(list(x))

b="My name is ganesh"
print(b.split())

c="class-class-class"
delimiter= "-"
print(c.split(delimiter))

a="doctor"
b="doctor"
a is b
print(a is b)

a=[1,2,3,4]
b=[1,2,3,4]
a is b
print(a is b)

a=[4,5,6,7,8]
b=[4,5,6,7,8]
print(id(a))
print(id(b))

a="doctor"
b="doctor"
print(id(a))
print(id(b))

a=[2,4,6,8,10]
b=a       #Aliasing
print(a is b) 

a[0]=22
print(b)







