#User function Template for python3
arr = tuple(map(int, input().split()))

########### Write your code below ###############
# Print "True" if all elements of tuple are different, otherwise print "False"
num = 0
for i in arr:
    num = i
    count = arr.count(num)
    
    
if count > 1: 
    print("False")
else: 
    print("True")
########### Write your code above ###############