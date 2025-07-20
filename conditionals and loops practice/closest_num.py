import math
class Solution:
    def closestNumber(self, n, m):
        # code here 
        q = n // m
        
        x = q * m
        
        a = m * (q + 1)
       
        
        if abs(n-x) < abs(n - a):
            return x
        elif abs(n-x) >  abs(n-a) :
            return a
        else:
            return x if abs(x) > abs(a) else a
