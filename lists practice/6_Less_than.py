def lessThan(arr, k):
    #code here
    ans = []
    for i in range(len(arr)):
        ele = arr[i]
        if ele < k:
            ans.append(ele)
    return ans
