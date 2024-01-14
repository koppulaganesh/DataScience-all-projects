#File Handling: Reading,Writing,deleting,creating of a files is known as file handling.
'''
open
read/write
close
'''
s=open("kala.text",mode='r')#r=read
print(s.read())
s.close()

s=open("kala.text",mode='w') #w=write
print(s.write("kal mithe hai okay nah bhai...."))
s.close()

s=open("kala.text",mode='a') #a=append
print(s.write("bye bye..!"))
s.close()

s=open("kala.text",mode='r+') #read and write
print(s.read())
print(s.write("bye bye..!"))
s.close()
