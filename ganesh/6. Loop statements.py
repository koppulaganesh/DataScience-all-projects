#Loop_statements or Iteration
'''
1. for loop
2. while loop
3. nested loop
'''
#for:- for loop is for element loop mentioned.
a=[20,21,22,23] #"[]" represents "tupple".
for i in a:
    print(i)

#range:-
for i in range (0,5): #In range of zero to five
    print(i)

for i in range (0,10,2): #'2' represents even numbers.
    print(i) 
#In the o/p we get only even numbers in the range of zero to ten.
#Note: In for loop only we use "range"

#while_loop:- 'for loop' is infinite loop of the object.
#ex:-
K=10
while 21<20:
    print("Hello")
#there is no output bcoz K=21 value is not less than 20
#Note: In 'while loop' we dont use "range"

T=20
while T<40:
    print("Hi")
    T+=1 #'assignment operator' used to stop the infinite loop.

#nested loop (for loop):- loop lo loop hahahaah :)
for i in range(0,10):
    for j in range(0,20):
        print(i+j)










