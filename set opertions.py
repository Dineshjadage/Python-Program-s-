
"""Program to demonstrate set opertions"""

s1={1,2,3}
s2={2,3,4}
#union
s3=s1.union(s2)
print("s1=",s1)
print("s2=",s2)

print("s1 union s2",s3)
#intersection
s3=s1.intersection(s2)
print("s1 intersection s2",s3)
print("s1=",s1)

#intersection_update
s1.intersection_update(s2)
print("s1 intersection_update s2",s1)
print("s1=",s1)

#difference
s1={1,2,3}
s2={2,3,4}

s3=s1.difference(s2)
print("s1 difference s2",s3)

s3=s2.difference(s1)
print("s2 difference s1",s3)

s3=s1.symmetric_difference(s2)
print("s1 symmetric_difference s2",s3)

#Relational Operators in sets
s1={1,2,3,4,5,6}
s2={2,3,4}
print("s1=",s1)
print("s2=",s2)
print("s1==s2",s1==2)
print("s1!=s2",s1!=s2)
print("s1>=s2",s1>=s2)
print("s1>s2",s1>=s2)
print("s1<=s2",s1<=s2)
print("s1<s2",s1<s2)


#Membership OPerators in set
print("1 in s1",1 in s1)
print("1 not in s1",1 not in s1)

output
s1= {1, 2, 3}
s2= {2, 3, 4}
s1 union s2 {1, 2, 3, 4}
s1 intersection s2 {2, 3}
s1= {1, 2, 3}
s1 intersection_update s2 {2, 3}
s1= {2, 3}
s1 difference s2 {1}
s2 difference s1 {4}
s1 symmetric_difference s2 {1, 4}
s1= {1, 2, 3, 4, 5, 6}
s2= {2, 3, 4}
s1==s2 False
s1!=s2 True
s1>=s2 True
s1>s2 True
s1<=s2 False
s1<s2 False
1 in s1 True
1 not in s1 False
