#User function Template for python3
n1 = int(input("num1 "))
n2 = int(input("num2 "))


# Your code here
a = n1
b = n2

for i in range(1,11):
    diff = n1 - n2
    print(diff, end=" ")
    n1 += a
    n2 += b


    