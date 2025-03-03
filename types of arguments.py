 """ program to demonstrate types of arguments"""

#default arguments
def myfun(a,b=20):
    res=a+b
    print("sum of a and b in my fun is",res)

a=10
myfun(a)

#required arguments
def aot(breadth,height):
    area=1/2*breadth*height
    print ("area of triangle is ",area)

breadth=20
height=30
aot(breadth,height)

#keyword argumnets
def fun1(firstname,lastname):
    print(firstname)
    print(lastname)

fun1(firstname="jack",lastname="dawson")

#variable length arguments
def sum(*n):
    total=0
    for i in n:
        total=total+i
    print(total)

sum()
sum(1,2)
sum(1,2,3)
sum(1,2,3,4)

"""output=
sum of a and b in my fun is 30
area of triangle is  300.0
jack
dawson
0
3
6
10"""
