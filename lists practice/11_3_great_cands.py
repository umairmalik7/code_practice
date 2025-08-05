#User function Template for python3

arr = [2,6,6,3,8,-1,3,4]
def maxProduct( arr):
    # code here
    arr.sort()
    arr.reverse()
    print(arr)

    a = max(arr)
    for i in range(len(arr)-1):
        b = arr[i]
        c = arr[i+1]
        if b < a:
            print(a*b*c)
            break
            
maxProduct(arr)