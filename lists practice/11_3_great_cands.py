#User function Template for python3

arr = [10,3,5,5,4,4,2,3]
def maxProduct( arr):
    # code here
    arr.sort()
    arr.reverse()
    print(arr)

    a = max(arr)
    for i in range(len(arr)):
        b =  arr[i]
        c = arr[i+1]
        if b < a:
            if c <= b:
                print(a*b*c)
                break

            
        
            
maxProduct(arr)