"""program to demonstrate call by value and call by reference"""

def cbv(a):
    a=a+1
    print("value of a in cbv is ",a)

def cbr(list1):
    list1.append(100)
    print("list1 in cbr",list1)

#call by value
a=10
print("cbv before calling",a)
cbv(a)
print("cbv after calling",a)

#call by reference
list1=[30,20,5,10]
print("list1 before calling cbr is",list1)
cbr(list1)
print("list1 after calling cbr is",list1)

"""output:
cbv before calling 10
value of a in cbv is  11
cbv after calling 10
list1 before calling cbr is [30, 20, 5, 10]
list1 in cbr [30, 20, 5, 10, 100]
list1 after calling cbr is [30, 20, 5, 10, 100]"""

