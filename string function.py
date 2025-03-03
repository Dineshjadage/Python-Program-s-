"""program to demonstrate string function"""

s1="roger"
print("s1 string is",s1)

#length
print("length of string s1 ",s1)

#capitalize
print("using capitalize",s1.capitalize())

#count
print("using count of r in s1",s1.count('r'))

#find
print("using find for e in s1",s1.find('e'))

#index
print("using index for r in s1",s1.find('r'))

#lower
print("using lower ",s1.lower())

#upper
print("using upper",s1.upper())

#replace
print("using replace r with s",s1.replace('r','s'))

#join
print("using join s1 and s2",s1.join("fed"))

#isalnum
print("using isalnum ",s1.isalnum())

#isalpha
print("using isalpha ",s1.isalpha())

#isdigit
print("using isdigit ",s1.isdigit())

#islower
print("using islower ",s1.islower())

#isupper
print("using isupper ",s1.isupper())

"""output:
s1 string is roger
length of string s1  roger
using capitalize Roger
using count of r in s1 2
using find for e in s1 3
using index for r in s1 0
using lower  roger
using upper ROGER
using replace r with s soges
using join s1 and s2 frogererogerd
using isalnum  True
using isalpha  True
using isdigit  False
using islower  True
using isupper  False"""
















