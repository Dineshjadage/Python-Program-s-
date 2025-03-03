
"""Program to demonstrate tuple functions"""

#creating,datatype,length of the tuple
t1=(1,2,3,4,1)
print(t1)
print(type(t1))
print("Length of the tuple",len(t1))

#reversed tuple
t2=reversed(t1)
print("Reversed tuple",tuple(t2))

#index
i=t1.index(1)
print("index of 1",i)

#slice
s1=t1[2:4]
print("slice[2:4]",s1)

#max and min
print("max in tuple",max(t1))
print("min in tuple",min(t1))

#sorted
s1=sorted(t1)
print("After sorting",s1)

s1=tuple(reversed(sorted(t1)))
print("After sorting and reversing",s1)

c1=t1.count(1)
print("count of 1s is",c1)

print("Element at location 3 is",t1[3])
print("Element at location -3 is",t1[-3])

"""Output:

(1, 2, 3, 4, 1)
<class 'tuple'>
Length of the tuple 5
Reversed tuple (1, 4, 3, 2, 1)
index of 1 0
slice[2:4] (3, 4)
max in tuple 4
min in tuple 1
After sorting [1, 1, 2, 3, 4]
After sorting and reversing (4, 3, 2, 1, 1)
count of 1s is 2
Element at location 3 is 4
Element at location -3 is 3"""

