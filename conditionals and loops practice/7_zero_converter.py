num = int(input("Enter an integer: "))
def pos(n):
    ## Write the code
    x = n - 1
    while(x > -1):
        print(x, end=" ")
        x -= 1
pos(num)

def neg(n):
    
    x = n 
    while(x < 1):
        print(x, end=" ")
        x += 1

neg(num)
