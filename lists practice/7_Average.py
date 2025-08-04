#User function Template for python3

def nonNegativeAverage(arr):
    
    #Write your code to find average of positive numbers in number list
    #Return the answer
    arr2 = []
    for i in range(len(arr)):
        if arr[i] >= 0:
            arr2.append(arr[i])
            
    add = 0       
    for i in range(len(arr2)):
        add =  add + arr2[i]
        avg = add / len(arr2)
    return avg
           