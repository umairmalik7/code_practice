num = int(input("int: "))

def printPattern(n):
    #Code here
    print("*")
    for i in range(n-2):
        print("*",end = " ")
        for j in range(i):
            print("  ",end="")
        for k in range(1):
            print("*",end="")
        print(" ")
    if n > 1:
        line = "* " * n
        print(line.strip())




printPattern(num)