"""program to demonstrate bulit in errors"""

try:
    res=2/0
    print(res)
except ArithmeticError:
    print("Divide by zero error")
print("End of program")

try:
    list1=[2,5,8]
    print(list1[1])
    print(list[7])
except LookupError:
    print("out of bounds")
print("End of program")

"""output:
Divide by zero error
End of program
5
out of bounds
End of program"""
