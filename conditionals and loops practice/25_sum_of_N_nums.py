class Solution:
    def sumOfNumbers(self, n):
        # code here
        add = 0
        for i in range(1,n+1):
            add += i
        return add