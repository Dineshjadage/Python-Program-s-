"""Program to genetate n terms fibonacci series"""

n=eval (input("Enter number of terms"))
n1=0
n2=1
print(n1)
print(n2)

for i in range (2,n):
    n3=n1+n2
    print(n3)
    n1=n2
    n2=n3

"""output:
Enter number of terms10
0
1
1
2
3
5
8
13
21
34"""
