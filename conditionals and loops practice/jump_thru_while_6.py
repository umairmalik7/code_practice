# Function to print x in increasing order
def printIncreasingPower(x):
    ##Your code here
    n = 1
    sqr =0
    # Loop to jump in powers of 2
    while(sqr <= x):
        ##Your code here
        sqr = n **2
        if sqr <= x:
            print(sqr , end = " ")
            n += 1
