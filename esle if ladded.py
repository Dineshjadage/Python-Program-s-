"""Program to find the result using esle if ladded"""

per=eval(input("Enter percentage"))
if(per>=75):
    print("Distinction")
elif(per>=60 and per<75):
    print("First Class")
elif(per>=50 and per<60):
    print("Second Class")
elif(per>=35 and per<50) :
    print("Pass Class")
else:
    print("Fail")

"""output=
Enter percentage90
Distinction"""
