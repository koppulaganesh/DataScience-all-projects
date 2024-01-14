#Dictionary: 
'''
1. It is defined by the curly brackets {}
2. key,value data type 
3. key is unique,immutable 
4. value is mutable(any data types)
5. Key will act as an index (no indexing)
6. No slicing
7. Dictionary is mutable.
ex: 
a={a1:"123",b2:"456"}
"a" is variable
"a1" is key 
"123" is the value

Key + value = item

'''
a={}
print(type(a)) #<class 'dict'>

b={1:"ganesh",2:"sahith",3:"ramulu",4:"rajamani"}
print(b[1])
print(b[2])
print(b[3])
print(b[4])

#dictionary methods:-
#1. get()
c={4:"apple",5:"mango",6:"kiwi"}
print(c.get(4)) #apple 
print(c.get(5)) #mango
print(c.get(6)) #kiwi

#2. keys()
d={1:"kcr",2:'ktr',3:"ntr",4:"anr"}
print(d.keys()) #dict_keys([1, 2, 3, 4])

#3. values()
d={1:"kcr",2:'ktr',3:"ntr",4:"anr"}
print(d.values()) #dict_values(['kcr', 'ktr', 'ntr', 'anr'])

#4. items()
d={1:"kcr",2:'ktr',3:"ntr",4:"anr"}
print(d.items())
#o/p: dict_items([(1, 'kcr'), (2, 'ktr'), (3, 'ntr'), (4, 'anr')])

#5. update()
d={1:"kcr",2:'ktr',3:"ntr",4:"anr"}
d.update({5:"cbn",6:"mgr",7:"cmr"})
print(d) #{1: 'kcr', 2: 'ktr', 3: 'ntr', 4: 'anr', 5: 'cbn', 6: 'mgr', 7: 'cmr'}

#for loop in dictionary:
d={1:"kcr",2:'ktr',3:"ntr",4:"anr"}
for i in d:
    print(i) # we get keys in the output

for i in {1:"kcr",2:'ktr',3:"ntr",4:"anr"}.values():
    print(i) # we get the out put of values.

for i in {1:"kcr",2:'ktr',3:"ntr",4:"anr"}.keys():
    print(i) #we get the keys in the output.
    
for i in {1:"kcr",2:'ktr',3:"ntr",4:"anr"}.items():
    print(i) # we get both keys and values in the output.





