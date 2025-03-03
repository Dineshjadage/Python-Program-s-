"""program to demonstrate arithmetic operation using split function"""

n1,n2=input("enter number").split()
n1=int(n1)
n2=int(n2)

add=n1+n2
print("addition is",add)

sub=n1-n2
print("substraction is ",sub)

mul=n1*n2
print("multiplication is",mul)

div=n1/n2
print("division is",div)

mod=n1%n2
print("mod is",mod)


"""output
enter number10 20
addition is 30
substraction is  -10
multiplication is 200
division is 0.5
mod is 10"""