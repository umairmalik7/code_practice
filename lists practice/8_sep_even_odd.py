#User function Template for python3

def evenOdd(arr):
    even = []
    odd = []

    #Write your code below to append odd elements in numbers to odd list
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            even.append(arr[i])
    #Write your code below to append even elements in numbers to even list
        else:
            odd.append(arr[i])
    

    return (odd,even)  #This is the return statement
