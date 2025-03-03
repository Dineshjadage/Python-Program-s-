"""Program to demonstrate list Operations"""
list1=[10,20,30,20,100]
list2=[30,40,60]

print(list1)
print(list2)

#Concatination
list3=list1+list2
print("After Concatnation",list3)

#Repetation
list3=list1*2
print("After Repetation",list3)

#Relational Operators
print("list1==list2",list1==list2)
print("list1!=list2",list1!=list2)
print("list>=list2",list1>=list2)
print("list1>list2",list1>list2)
print("list<=list2",list1<=list2)
print("list1<list2",list1<list2)

#Membership Operators
print("10 in list1",10 in list1)
print("10 not in list1",10 not in list1)

#Postive Indexing
i=list1[2]
print("Positive Indexing element at location 2 is ",i)

#Negative Indexing
i=list1[-2]
print("Negative Indexing element at location -2 is ",i)

#Updating
list1[1]
print("After Updating",list1)

#Deleting
del list1[1]
print("After Deleting",list1)

#slicing
print("list1[2:4]",list1[2:4])
print("list1[2:]",list1[2:])
print("list1[:4]",list1[:4])
print("list1[-4:-2]",list1[-4:-2])

#Deleting all elements
#del list1
#print("After deleting all elements",list1)

"""Output:

[10, 20, 30, 20, 100]
[30, 40, 60]
After Concatnation [10, 20, 30, 20, 100, 30, 40, 60]
After Repetation [10, 20, 30, 20, 100, 10, 20, 30, 20, 100]
list1==list2 False
list1!=list2 True
list>=list2 False
list1>list2 False
list<=list2 True
list1<list2 True
10 in list1 True
10 not in list1 False
Positive Indexing element at location 2 is  30
Negative Indexing element at location -2 is  20
After Updating [10, 20, 30, 20, 100]
After Deleting [10, 30, 20, 100]
list1[2:4] [20, 100]
list1[2:] [20, 100]
list1[:4] [10, 30, 20, 100]
list1[-4:-2] [10, 30]"""

