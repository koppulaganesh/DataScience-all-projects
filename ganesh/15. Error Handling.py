#Error handling:
'''
1.Interrupting normal execution of a code is called error or exception
2.we can handle it through error handling
#There four types of blocks
1.try
2.except
3.else
4.finally 

'''
a=1
try:
    print(b) #risky code(may be there's an error)
except:
    print("ERROR")
else:
    print("NO ERROR")
finally:
    print("no problem") #it will always print irrespective of the result