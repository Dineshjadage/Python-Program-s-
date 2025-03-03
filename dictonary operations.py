"""program to demonstrate dictonary operations"""

d1={1:"jack",2:"rose"}
d2={"x":1,"y":2}

print(d1)
print(d2)

#Equality
print("d1==d2",d1==d2)
print("d2!=d2",d1!=d2)

#membership
print("1 in d1",1 in d1)
print("1 not in d1",1 not in d1)

"""output:
{1: 'jack', 2: 'rose'}
{'x': 1, 'y': 2}
d1==d2 False
d2!=d2 True
1 in d1 True
1 not in d1 False"""
