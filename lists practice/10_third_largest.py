class Solution:
    def thirdLargest(self,arr):
        # code here
    
        arr.sort()
        arr.reverse()
        a = max(arr)
    
        for i in range(len(arr)):
            b = arr[i]
            if len(arr) < 3:
                return -1
            elif b < a:
                if arr[2] <= b :
                    return arr[2]
        else:
            return arr[0]
