"""program to demonstarte array"""

from array import *

a=array('i',[2,1,3,5,6])
print(a)

#length
print("Length of array is ",len(a))

#inserting
a.insert(1,4)
print("After inserting 4 at loc 1 array is",a)

#append
a.append(1000)
print("After appending  1000 array is ",a)

#index
print("Element at location 1 is ",a[1])

#remove
a.remove(1000)
print("After removing element 1000 array is ",a)

a.pop()
print("After poping",a)

#delete
del a[1]
print("After deleting element at location 1 array ",a)

#find index
print("Location of 3 is",a.index(3))

#slicing
print("a[1:3]",a[1:3])
print("a[-3:-1]",a[-3:-1])

"""output:
array('i', [2, 1, 3, 5, 6])
Length of array is  5
After inserting 4 at loc 1 array is array('i', [2, 4, 1, 3, 5, 6])
After appending  1000 array is  array('i', [2, 4, 1, 3, 5, 6, 1000])
Element at location 1 is  4
After removing element 1000 array is  array('i', [2, 4, 1, 3, 5, 6])
After poping array('i', [2, 4, 1, 3, 5])
After deleting element at location 1 array  array('i', [2, 1, 3, 5])
Location of 3 is 2
a[1:3] array('i', [1, 3])
a[-3:-1] array('i', [1, 3])"""