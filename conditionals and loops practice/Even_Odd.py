#User function Template for python3
# Take n input and print who wins
num = int(input())

def even_odd(a):
    if a % 2 == 0:
        print("Friend")
    else:
        print("You")

even_odd(num)