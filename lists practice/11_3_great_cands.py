#User function Template for python3

class Solution:
    def maxProduct(self, arr):
        # code here
        arr.sort()
        x = min(arr)
        for i in range(1,len(arr)):
            y  = arr[i]
            if y >= x:
                pro2 = x*y
                break
        arr.reverse()
        a = max(arr)
        for i in range(1,len(arr)):
            b =  arr[i]
            c = arr[i+1]
            if b <=  a:
                if c <= b:
                    pro1 = a*b*c
                    break
        pro3 = a*pro2
        if pro1 > pro3:
            return pro1
        else:
            return pro3