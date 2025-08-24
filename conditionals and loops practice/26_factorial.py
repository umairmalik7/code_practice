n = int(input())

# Your code here

def factorial(n):
    fac = 1
    for i in range(1,n+1):
        fac *= i
    return fac


factorial(n)