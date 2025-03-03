"""Program to demonstarate set functions"""

x=set()                #Empty set
print(x)
print(type(x))


x=set([0,1,2,4,2,4])  #set with elements
print(x)

x={4,5,6,'jack','Rose'}
for val in x:
    print(val)

x={1,2,'Roger','Steffi','Virat'}
print(x)
print("Length of set is",len(x))

x.add('Sachin')#adding Sachin
print("After Adding Sachin",x)
print("Length of set is",len(x))

x.update(["Ronaldo","Messi"])  #adding Ronaldo
print("Ater adding Ronaldo and Messi",x)
print("length of set is",len(x))

x.remove("Messi")
print("After removing Messi",x)
print("Length of set is",len(x))


x.discard("Ronaldo")
print("Ater discharging Ronaldo",x)
print("Length of set is",len(x))

x.clear()
print("After clear",x)
print("Length of set is",len(x))

output:
set()
<class 'set'>
{0, 1, 2, 4}
jack
4
5
6
Rose
{'Virat', 1, 2, 'Roger', 'Steffi'}
Length of set is 5
After Adding Sachin {'Virat', 1, 2, 'Sachin', 'Roger', 'Steffi'}
Length of set is 6
Ater adding Ronaldo and Messi {'Virat', 1, 2, 'Sachin', 'Messi', 'Ronaldo', 'Roger', 'Steffi'}
length of set is 8
After removing Messi {'Virat', 1, 2, 'Sachin', 'Ronaldo', 'Roger', 'Steffi'}
Length of set is 7
Ater discharging Ronaldo {'Virat', 1, 2, 'Sachin', 'Roger', 'Steffi'}
Length of set is 6
After clear set()
Length of set is 0

