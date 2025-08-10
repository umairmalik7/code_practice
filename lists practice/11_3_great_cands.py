#User function Template for python3

arr = [-439 ,-284, -104 ,323, 554 ,382 ,139]
def maxProduct( arr):
    # code here
    arr.sort()
    x = min(arr)
    print("smallest value",x)
    for i in range(1,len(arr)):
        y  = arr[i]
        print("2nd smallest value",y)
        if y <= x:
            pro2 = x*y
            break
    
    
    arr.reverse()

    a = max(arr)
    print("maximum value", a)
    pro3 = a*pro2
    for i in range(len(arr)):
        b =  arr[i]
        c = arr[i+1]
        if b < a:
            if c <= b:
                pro1 = a*b*c
                break
                
    if pro1 > pro3:
        print("pro1", pro1)
    else:
        print("pro3",pro3)

maxProduct(arr)