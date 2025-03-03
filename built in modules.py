"""program to demonstrate built in modules"""
import math

#constants in math
print("Value of pi is",math.pi)
print("Value of euler is",math.e)

#function in math
print("factorial of 3 is ",math.factorial(3))
print("gcd of 6 and 4 is",math.gcd(6,4))
print("lcm of 6 and 4 is",math.lcm(6,4))
print("sqrt of 9 is ",math.sqrt(9))
print("pow 2,3 is ",math.pow(2,3))
print("floor of 4.3 is",math.floor(4.3))
print("ceil of 4.3 is",math.ceil(4.3))
print("sin90 is",math.sin(90))

import random
list1=[3,1,2,5,6,9]
print("Random number ",random.choice(list1))
random.shuffle(list1)
print("After shuffle ",list1)
print("Random integer range ",random.randint(2,10))
s="computer"
print("Random character is string",random.choice(s))

import emoji
print("\N{slightly smiling face}")
print("\N{winking face}")
print("\N{grinning face}")

"""output:
Value of pi is 3.141592653589793
Value of euler is 2.718281828459045
factorial of 3 is  6
gcd of 6 and 4 is 2
lcm of 6 and 4 is 12
sqrt of 9 is  3.0
pow 2,3 is  8.0
floor of 4.3 is 4
ceil of 4.3 is 5
sin90 is 0.8939966636005579
Random number  1
After shuffle  [2, 3, 6, 5, 1, 9]
Random integer range  6
Random character is string m
🙂
😉
😀"""





