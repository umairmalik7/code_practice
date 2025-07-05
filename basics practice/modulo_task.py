N = int(input("Enter an integer: "))

K = 1
while  K < N:
    x = N % K
    print( f" {N}%{K} = {x}")
    K += 1
   
if N == 1:
    print(K)
else: 
    print(K-1)
    