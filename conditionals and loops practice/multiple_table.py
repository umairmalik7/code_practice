#User function Template for python3
class Solution:
    def getTable(self,n):
        # code here
        table = []
        for i in range(1,11):
            res = n * i
            table.append(res)
            
        return table