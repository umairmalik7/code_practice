#User function Template for python3

arr = [-439 ,-284, -104 ,323, 554 ,382 ,139]
def maxProduct( arr):
    # code here
    arr2 = []
    for i in arr:
        a = abs(i)
        arr2.append(a)

    for i in range(len(arr)):
        arr[i] = arr2[i]
            
    arr.sort()
    arr.reverse()
    print(arr)
    x = max(arr)
    for i in range(len(arr)):
        b =  arr[i]
        c = arr[i+1]
        if b < x:
            if c <= b:
                print(x*b*c)
                break
maxProduct(arr)