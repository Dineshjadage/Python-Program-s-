""" Program to demonstrate Operation"""
a=20
b=10
print("a=%d b=%d" %(a,b))

#Arithmetic Operations
c=a+b                         #Addition Operator
print("Sum is ",c)
c=a-b                         #subtraction Operator 
print("Difference is ",c)
c=a*b                         #Multiplication Operaor
print("multiplication is ",c) 
c=a/b                         #Division Operator
print("Divide is ",c)
c=a%b                         #modulus Operator
print("Mod is ",c)


#Relational Operatorsprint
print("a>=b",a>=b) #Greater than or equal to
print("a>b",a>b)    #Greater than
print("a<=b",a<=b)    #Less than or equal to
print("a<b",a<b)    #less than
print("a==b",a==b)  #Equal to
print("a!=b",a!=b)  #Not Equal to


#Logical Operaters
x=50
y=60
print("a>b and x>y",(a>b)and(x>y))     #logical and operator
print("a>b or x>y",(a>b)or(x>y))       #Logical or Operator
print("not (a>b)",not(a>b))            #Logiacal or operator



#Bitwise OperatorS
x=1
y=3
print("(x&y)",(x&y))         #Bitwise and
print("(x|y)",(x|y))         #Bitwise or
print("(x^y)",(x^y))         #Bitwise xor
print("x<<2",(x<<2))         #Bitwise left shift
print("x>>1",(x>>1))         #Bitwise right shift 


#String Operation
s="Python"
print("Repetation",s*3)      #Repatation
print("slice",s[3])          #slice
print("range",s[2:5])        #range
s=s +" is strong"
print("concatination",s)    #concatination



#membership operator
print("is" in s)
print("is"not in s)


"""output:

a=20 b=10
Sum is  30
Difference is  10
multiplication is  200
Divide is  2.0
Mod is  0
a>=b True
a>b True
a<=b False
a<b False
a==b False
a!=b True
a>b and x>y False
a>b or x>y True
not (a>b) False
(x&y) 1
(x|y) 3
(x^y) 2
x<<2 4
x>>1 0
Repetation PythonPythonPython
slice h
range tho
concatination Python is strong
True
False"""
