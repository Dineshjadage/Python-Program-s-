"""Program to demonstrate list functions"""

list1=[10,20,50,90,5]
print(list1)

#Length
print("Length of list",len(list1))

#Appending
list1.append(100)
print("After appending",list1)

#Inserting
list1.insert(2,300)
print("After Inserting",list1)

#Extending
list1.extend([700,800])
print("After Extending",list1)

#remove
list1.remove(100)
print("After removing",list1)

#pop
list1.pop()
print("After poping",list1)

#index
i=list1.index(300)
print("index of 300 is",i)

#count
c=list1.count(10)
print("counts of 10 is",c)

#sort
list1.sort()
print("After sorting",list1)

#reverse
list1.reverse()
print("After reversing",list1)

#sum
total=sum(list1)
print("total of elements in list",total)

"""output:-

[10, 20, 50, 90, 5]
Length of list 5
After appending [10, 20, 50, 90, 5, 100]
After Inserting [10, 20, 300, 50, 90, 5, 100]
After Extending [10, 20, 300, 50, 90, 5, 100, 700, 800]
After removing [10, 20, 300, 50, 90, 5, 700, 800]
After poping [10, 20, 300, 50, 90, 5, 700]
index of 300 is 2
counts of 10 is 1
After sorting [5, 10, 20, 50, 90, 300, 700]
After reversing [700, 300, 90, 50, 20, 10, 5]
total of elements in list 1175"""
