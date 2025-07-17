import math

num = int(input("Enter int: "))
mod = int(input("Enter mod: "))
def closestNumber( n, m):
        # code here 
    if m != 0:
        for i in range(n-1,0,-1):
            if i % m == 0:
                print(f"the value of i = {i}")
                y  = math.isclose(i,n,rel_tol=0.4)
                print(y)
                if y == True: break
        for j in range(n+1,n+10):
            if j % m == 0:
                print(f"the value of j = {j}")
                x = math.isclose(j,n,rel_tol=0.3)
                print(x)
                if x == True: break
        if n - i < j - n:
            print(i)
        else:
            print(j)
    else:
        return n

closestNumber(num, mod)

