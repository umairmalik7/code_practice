a = list(map(int, input().split()))
b = list(map(str, input().split()))
query = list(map(int, input().split()))
dict = {}
for i in range(len(a)):
    dict[a[i]] = b[i]
        
ans = []
for key in range(len(query)):
    ########### Write your code below ###############
    # get value for given key
    x = query[key]
    val = dict.get(x)
    ########### Write your code above ###############
    
    # append to ans
    ans.append(val)

# Print ans
print(*ans, sep='\n')