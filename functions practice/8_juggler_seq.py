import math
class Solution:
    def jugglerSequence(self, n):
        # code here
        arr = []
        arr.append(n)
        while n != 1:
            if n % 2 == 0:
                n = math.floor(math.sqrt(n))
                arr.append(n)
              
            else:
                n =  math.floor(n * math.sqrt(n))
                arr.append(n)
                
        
        return arr
                
