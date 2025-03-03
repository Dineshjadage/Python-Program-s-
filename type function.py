"""program to demonstrate type function"""

a=10
b=1.0
c="hello"

print(type(a))
print(type(b))
print(type(c))

x,y,z=input("enter 3 values").split()
x=eval(x)
y=eval(y)
z=eval(z)
print(x,type(x))
print(y,type(y))
print(z,type(z))


"""output

<class 'int'>
<class 'float'>
<class 'str'>
enter 3 values"hi" 1 1.0
hi <class 'str'>
1 <class 'int'>
1.0 <class 'float'>"""
