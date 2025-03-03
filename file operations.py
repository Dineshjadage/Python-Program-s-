"""program to demonstrate file operations"""
#Read a file
fileptr=open("f.txt","r")
content=fileptr.read()
print(content)
print(fileptr.tell())
fileptr.seek(0)
content=fileptr.readline()
print(content)
print(fileptr.tell())
fileptr.close()

#write to file
fileptr=open("f1.txt","w")
fileptr.write("hello Jack\n")
fileptr.write("How are you")
fileptr.close()

fileptr=open("f1.txt","r")
content=fileptr.read()
print(content)
fileptr.close()

#append to file
fileptr=open("f1.txt","a")
fileptr.write("\nI an fine")
fileptr.close()

fileptr=open("f1.txt","r")
content=fileptr.read()
print(content)
fileptr.close()

"""output:
Mumbai
new york
16
Mumbai

8
hello Jack
How are you
hello Jack
How are you
I an fine"""
