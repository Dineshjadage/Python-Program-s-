"""program to demonstrate Numpy functions"""
import numpy as np

#rounding Functions
a1=[1.234,2.345,3.678]
print("a1=",a1)
print("using numpy around ",np.around(a1))
print("using numpy around ",np.around(a1,2))
print("using numpy trunc ",np.trunc(a1))
print("using numpy floor ",np.floor(a1))
print("using numpy ceil ",np.ceil(a1))

#Arithmetic Functions
a1=np.array([2,4,6])
a2=np.array([1,2,3])
print("a1=",a1)
print("a2=",a2)
res=np.add(a1,a2)
print("after adding a1 and a2 res is",res)
res=np.subtract(a1,a2)
print("after subtracting a1 and a2 res is",res)
res=np.multiply(a1,a2)
print("after multiplying a1 and a2 res is",res)
res=np.divide(a1,a2)
print("after adding a1 and a2 res is",res)
res=np.mod(a1,a2)
print("after mod a1 and a2 res is",res)
res=np.power(a1,a2)
print("after power a1 and a2 res is",res)
res=np.negative(a1,a2)
print("after negative a1 and a2 res is",res)

#special Functions
a1=[-2,3,4,1000]
print("a1=",a1)
print("cube root of a1 is ",np.cbrt(a1))
print("square of a1 is ",np.square(a1))
print("absolute of a1 is ",np.absolute(a1))

#Trignometric Functions
a1=[0,90,180,270,360]
print("a1=",a1)
print("sin values of a1 is ",np.sin(a1))
print("cos values of a1 is ",np.cos(a1))
print("tan values of a1 is ",np.tan(a1))

"""output:
a1= [1.234, 2.345, 3.678]
using numpy around  [1. 2. 4.]
using numpy around  [1.23 2.35 3.68]
using numpy trunc  [1. 2. 3.]
using numpy floor  [1. 2. 3.]
using numpy ceil  [2. 3. 4.]
a1= [2 4 6]
a2= [1 2 3]
after adding a1 and a2 res is [3 6 9]
after subtracting a1 and a2 res is [1 2 3]
after multiplying a1 and a2 res is [ 2  8 18]
after adding a1 and a2 res is [2. 2. 2.]
after mod a1 and a2 res is [0 0 0]
after power a1 and a2 res is [  2  16 216]
after negative a1 and a2 res is [-2 -4 -6]
a1= [-2, 3, 4, 1000]
cube root of a1 is  [-1.25992105  1.44224957  1.58740105 10.        ]
square of a1 is  [      4       9      16 1000000]
absolute of a1 is  [   2    3    4 1000]
a1= [0, 90, 180, 270, 360]
sin values of a1 is  [ 0.          0.89399666 -0.80115264 -0.17604595  0.95891572]
cos values of a1 is  [ 1.         -0.44807362 -0.59846007  0.98438195 -0.28369109]
tan values of a1 is  [ 0.         -1.99520041  1.33869021 -0.17883906 -3.38014041]"""

