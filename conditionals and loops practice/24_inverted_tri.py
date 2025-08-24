num = int(input("int: "))

def printPattern( n):
        #Code here
        for i in range(n):
            print("*",end=" ")
            for j in range(n-i,1,-1):
                print("*",end=" ")
            print()


printPattern(num)