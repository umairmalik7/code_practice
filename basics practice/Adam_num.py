import math

num = input("Enter a number")
def checkAdamOrNot( N):
        # code here 
        if N is int:
            sqofN = math.exp(N)
        else:
            isqofN = int(N)
            sqofN = math.exp(math.ceil(isqofN))


        reverse = sqofN.reverse()
        sq_root = math.sqrt(reverse)
        revSqRoot = sq_root.reverse(round(sq_root))
        if N == revSqRoot:
            print("true")
        else:
            print("False")
        
checkAdamOrNot(num)