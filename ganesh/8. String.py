#String:- Collection of characters. Str is immutable in nature.
#it allows indexing.
'''
Types of declaring the string:--
1. single quotes
2. double quotes
3. triple quotes
'''
a='GANESH'
b="GANESH"
c='''GANESH'''
print(type(a)) #o/p <class 'str'>
print(type(b)) #o/p <class 'str'>
print(type(c)) #o/p <class 'str'>
print(id(a))
print(id(b))
print(id(c))

#string method:
#1.lower()
jgkoppula="gmail"
print(jgkoppula.upper())

#2. upper()
Virat="CAPTAIN"
print(Virat.lower())

#3. startswith()
python="programming language"
print(python.startswith("programming"))

#4. endswith()
python="programming language"
print(python.endswith("language"))

#5. replace()
sachin="God of Criket"
print(sachin.replace("God","Lord"))

#6. index()
python="programming language"
print(python.index("programming")) #we get output as "zero"
print(python.index("software")) #we get output as an error

#7. find()
python="programming language"
print(python.find("programming")) #we get o/p as "zero"
print(python.find("ganesh")) #we get o/p as "-1"

#8. count()
BRS="Baratiya Rashtra Samithi"
print(BRS.count("a")) #o/p: 6 ( 'a' repeated for 6 times)
#count is used to find the letter count how many time it got repeated.

#9. removeprefix
python="van russom"
print(python.removeprefix("van"))

#10. removesuffix
leaf="Ranapala Aku"
print(leaf.removesuffix("Aku"))

#11. split 
#converts string data type to list
fruits="apple grapes mango"
print(fruits.split())

#12. strip (trim)
name="     Koppula Ganesh   "
print(len(name)) #o/p 22
print(name.strip()) #o/p:Koppula Ganesh
v=name.strip()
print(len(v)) #o/p 14

#13. lstrip (left trim)
name2="       Mettu Ramulu"
print(len(name2))
print(name2.lstrip())
p=name2.lstrip()
print(len(p))

#14. rstrip (right trim)
name3="Koppula Rajamani      "
print(len(name3))
print(name3.rstrip())
j=name3.rstrip()
print(len(j))


