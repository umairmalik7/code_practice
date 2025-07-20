import math

num = int(input("Enter int: "))
mod = int(input("Enter mod: "))
def closestNumber( n, m):
        # code here 
    if m != 0:
        for i in range(n,n-100000,-1):
            if i % m == 0:
                print(f"the value of i = {i}")
                y  = math.isclose(i,n,rel_tol=0.5)
                if y == True: break
        for j in range(n,n+100000):
            if j % m == 0:
                print(f"the value of j = {j}")
                x = math.isclose(j,n,rel_tol=1)
                if x == True: break
        
        if n > 0:
            if n - i > j - n or j == n:
                print("first",j)
            elif i -n == j -n and j > i:
                print("sec",j)
            else:
                print(i)
        elif n <= 0:
            
            
           
            x = abs(n-i)
            y = abs(n-j)
            
            if x > y or y == n:
                print("first",j)

            elif x == y  and  abs(i) > abs(j):
                print("second",i)
            else:
                print("last",i)
    
    else:
        return n

closestNumber(num, mod)

