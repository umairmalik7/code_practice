#User function Template for python3
import math

class Solution:
    def checkAdamOrNot(self, N):
        # code here 
        isqofN = int(N)
        sqofN = isqofN**2
        sqofN = str(sqofN)
        

        reverse = int(sqofN[::-1])
        sq_root = str(int(math.sqrt(reverse)))
        revSqRoot = sq_root[::-1]
        if N == int(revSqRoot):
            return "YES"
        else:
            return "NO"