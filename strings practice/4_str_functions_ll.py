# Function to check if string
# starts and ends with 'gfg'
def gfg(S):
    b = S.lower()
    start = b.startswith("gfg")
    end = b.endswith("gfg")
    if start and  end :
        print("Yes")
    else:
        print("No")