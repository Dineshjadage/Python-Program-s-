"""program to find factorial of a number"""

n=eval(input("Enter the number"))
fact=1

if(n==0):
    print("Factorial is 1")
else:
    while(n!=0):
        fact=fact*n
        n=n-1
    print("Factorail is ",fact)

"""output:
Enter the number12
Factorail is  479001600"""