"""Program to demonstrate tuple operations"""

t1=(4,3,2,1,4)
t2=(2,3)

print(t1)
print(t2)

#Concatination
t3=t1+t2
print("After Concatination",t3)

#Repetation
t3=t2*2
print("After Repetation",t3)

#Relational Operators with tuples
print("t1==t2",t1==t2)
print("t1!=t2",t1!=t2)
print("t1>=t2",t1>=t2)
print("t1>t2",t1>t2)
print("t1<=t2",t1<=t2)
print("t1<t2",t1<t2)

#Membership Operators
print("10 in t1",10 in t1)
print("10 not in t1",10 not in t1)

#Packing
a=10
b=20
c=30

t3=a,b,c
print("After Packing",t3)

#Unpacking
p,q,r=t3
print("After Unpacking",p,q,r)

"""Output:-

(4, 3, 2, 1, 4)
(2, 3)
After Concatination (4, 3, 2, 1, 4, 2, 3)
After Repetation (2, 3, 2, 3)
t1==t2 False
t1!=t2 True
t1>=t2 True
t1>t2 True
t1<=t2 False
t1<t2 False
10 in t1 False
10 not in t1 True
After Packing (10, 20, 30)
After Unpacking 10 20 30"""
