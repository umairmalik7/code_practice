class Solution:    
    def printNos(self,n):
        #Code here
        if n == 0:
            return 0
        else:
            self.printNos(n-1)
            print(n, end=" ")
