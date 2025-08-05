#User function Template for python3

class Solution:
    def series(self, n):
        # code here
        a = 0
        b = 1
        fib = [0,1]
        for i in range(n-1) :
            c = (a + b) % 1000000007
            a = b
            b = c
            fib.append(c)
       
        return fib