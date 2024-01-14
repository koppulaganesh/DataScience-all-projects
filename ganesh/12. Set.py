#Set: Sets are used to store multiple items in a single variable.
'''
1.set is defined by curly brackets {}
2.it do not allow duplicates
3.No index, unordered, slicing is not possible
4.Do not allow mutable data types as set elements.
Note: Sets are unordered, so we cannot be sure in which order the items will appear.

'''
a={}
print(type(a)) #<class 'dict'>
#Note: based on the elements it will decide as "set" untill that it is "dictionary" only.

b={1,2,3,4,5,4,3,2,1,1,7,8,9,0}
print(type(b)) #<class 'set'>
print(b) #{0, 1, 2, 3, 4, 5, 7, 8, 9} 
#we have no repeatation of elements in o/p

#set methods:
#1. add() :- we can add single element.
b={23,34,56,67,8,9,98,7,6,5,5,5,4}
b.add(123)
print(b) 
#o/p: {34, 67, 98, 5, 6, 7, 8, 9, 4, 23, 56, 123}

#2. update() :- we can add the bulk data at once.
c={1,2,3,3,4,5,6}
c.update({7,8,9})
print(c) #{1, 2, 3, 4, 5, 6, 7, 8, 9}

#3. pop() :- it will remove any one of the elements randomly.
d={1,2,3,4,5,6,7,8,}
d.pop()
print(d) #{2, 3, 4, 5, 6, 7, 8}

#4.remove() :- it is used to remove the particular element we mention.
e={1,1,2,3,4,5,6,7,78,8,8,8,8,}
e.remove(78)
print(e) #{1, 2, 3, 4, 5, 6, 7, 8}

#note: discard() is also used to delete the specified element.
e={1,1,2,3,4,5,6,7,78,8,8,8,8,}
e.discard(8)
print(e) #o/p:- {1, 2, 3, 4, 5, 6, 7, 78}

#5. clear()
e={1,1,2,3,4,5,6,7,78,8,8,8,8,}
e.clear()
print(e)

#set operations:-
#1. Union:-
set1={1,2,3}
set2={4,5,6}
print(set1.union(set2))  #{1, 2, 3, 4, 5, 6}

#2.intersection:-
set1={1,2,3,4,5}
set2={4,5,6}
print(set1.intersection(set2)) #{4, 5} 
#the two elements which are common in both set1 and set2 will get as output.

#3. difference:-
set3={1,2,3,4,5,6,7,8}
set4={5,6,7,8,9,10}
print(set3.difference(set4)) #{1, 2, 3, 4}
#the left over elements in set3 except common in both sets. 

#4. issubset:-
set1={1,3,4,6}
set2={1,2,3,4,5,6,7,8,9,10}
print(set1.issubset(set2)) #True

#5. issuperset:-
set1={1,2,3,4,5,6}
set2={1,2,3,4,5,6,7,8,9,10}
print(set2.issuperset(set1)) #True

#for loop in set:-
b={1,2,3,4,5,6,7}
for i in b:
    print(i)

fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
    print("yes")
    