"""program to demonstrate dictonary functions"""
#creating dictonary
d={1:"jack",2:"Rose",3:"Tom","x":1,"y":2,"z":3}
print(d)
print(type(d))

#length
print("length is",len(d))

#keys
keys=list(d.keys())
print("keys",keys)
print(keys[2])

#values
values=list(d.values())
print("values",values)

#get
print("using get",d.get("x"))

#update
d["x"]=10
print("updating x",d)
d.update({1:"jerry"})
print("updating 1",d)

#delete
del d["x"]
print("deleting x",d)

#pop
d.pop(2)
print("pop(2)",d)

#popitem
d.popitem()
print("popitem",d)

"""output:
{1: 'jack', 2: 'Rose', 3: 'Tom', 'x': 1, 'y': 2, 'z': 3}
<class 'dict'>
length is 6
keys [1, 2, 3, 'x', 'y', 'z']
3
values ['jack', 'Rose', 'Tom', 1, 2, 3]
using get 1
updating x {1: 'jack', 2: 'Rose', 3: 'Tom', 'x': 10, 'y': 2, 'z': 3}
updating 1 {1: 'jerry', 2: 'Rose', 3: 'Tom', 'x': 10, 'y': 2, 'z': 3}
deleting x {1: 'jerry', 2: 'Rose', 3: 'Tom', 'y': 2, 'z': 3}
pop(2) {1: 'jerry', 3: 'Tom', 'y': 2, 'z': 3}
popitem {1: 'jerry', 3: 'Tom', 'y': 2}"""
