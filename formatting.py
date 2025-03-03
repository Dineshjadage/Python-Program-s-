"""program to demontrate formatting"""

#fFormatting using mod operator
pi=3.142
print("pi value is %3.3f" %pi)

x=10
print("value of x is %10d" %x)

#Formatting using format method
print("python is {} language".format("simple"))

print("value of {:%}".format(0.76))
print("value of {:.0%}".format(0.76))

print("hexadecimal value of {0} is {0:x}".format(11))
print("octal value of {0} is {0:o}".format(10))
print("binary value of {0} is {0:b}".format(2))

print("decimal value of hexadecimal b is {0:d}".format(0xb))
print("decimal value of octal 12 is {0:d}".format(0o12))
print("decimal value of binary 10 is {0:d}".format(0b10))

#formatting using string method
s="python"
print(s.center(10,'#'))
print(s.ljust(10,'#'))
print(s.rjust(10,'#'))      


"""Output
pi value is 3.142
value of x is         10
python is simple language
value of 76.000000%
value of 76%
hexadecimal value of 11 is b
octal value of 10 is 12
binary value of 2 is 10
decimal value of hexadecimal b is 11
decimal value of octal 12 is 10
decimal value of binary 10 is 2
##python##
python####
####python"""
