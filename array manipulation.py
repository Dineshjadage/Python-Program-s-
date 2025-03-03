"""program to demonstarte array manipulation"""

import numpy as np

a=np.arange(4).reshape(2,2)
print("2*2 array\n",a)

#Arithmetic operations
print("adding 1 to array a\n",a+1)
print("substracting 1 to array a\n",a-1)
print("multipling 1 to array a\n",a*1)

#matrix functions
a1=np.arange(12).reshape(4,3)
print("4*3 array\n",a1)
print("transpose of a1 is \n",np.transpose(a1))
print("swap axes of a1 is \n",np.swapaxes(a1,1,0))

#resize of array
a=np.array([[1,2,3],[4,5,6]])
print("New array 2*3 is \n",a)
print("resize of array \n",np.resize(a,(3,2)))

#appending
a=np.append(a,[7,8,9])
print("after appending \n",a)
print("resize of array \n",np.resize(a,(3,3)))

#inserting
a=np.insert(a,3,[10,11,12])
a=np.resize(a,(4,3))
print("after inserting at loc 3\n",a)

#deleting
a=np.resize(a,(4,3))
a=np.delete(a,1,0)
print("after deleting row 1 \n",a)

#Max and Min
print("Min element is ",np.amin(a))
print("Max element is ",np.amax(a))

"""output:
2*2 array
 [[0 1]
 [2 3]]
adding 1 to array a
 [[1 2]
 [3 4]]
substracting 1 to array a
 [[-1  0]
 [ 1  2]]
multipling 1 to array a
 [[0 1]
 [2 3]]
4*3 array
 [[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 9 10 11]]
transpose of a1 is 
 [[ 0  3  6  9]
 [ 1  4  7 10]
 [ 2  5  8 11]]
swap axes of a1 is 
 [[ 0  3  6  9]
 [ 1  4  7 10]
 [ 2  5  8 11]]
New array 2*3 is 
 [[1 2 3]
 [4 5 6]]
resize of array 
 [[1 2]
 [3 4]
 [5 6]]
after appending 
 [1 2 3 4 5 6 7 8 9]
resize of array 
 [[1 2 3]
 [4 5 6]
 [7 8 9]]
after inserting at loc 3
 [[ 1  2  3]
 [10 11 12]
 [ 4  5  6]
 [ 7  8  9]]
after deleting row 1 
 [[1 2 3]
 [4 5 6]
 [7 8 9]]
Min element is  1
Max element is  9"""






