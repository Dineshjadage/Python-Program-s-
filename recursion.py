"""program to demonstrate recursion"""
def rec(n):
    if(n==0):
        return
    else:
        n=n-1
        print(n)
        rec(n)


n=3
rec(n)

output:
2
1
0