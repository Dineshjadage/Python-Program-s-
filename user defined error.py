"""program to demonstrate user defined error"""

class AgeError(Exception):
    "Raised AgeError"
    pass

age=eval(input("Enter Age"))
try:
    if age<18:
        raise AgeError
    else:
        print("Eligible to vote")
except AgeError:
    print("Not Eligible to vote")
print("End of program")

"""output:
Enter Age5
Not Eligible to vote
End of program"""
