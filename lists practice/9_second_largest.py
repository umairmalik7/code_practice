class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        arr.sort()
        arr.reverse()
        a = max(arr)
        for i in range(len(arr)):
            if arr[i] < a:
                return arr[i]
        else:
            return -1