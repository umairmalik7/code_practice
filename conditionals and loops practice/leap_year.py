#User function Template for python3
# Take year input and print if year is a leap year
year = int(input())

def leap_year(y):
    if y % 4 == 0:
        if y % 100 != 0:
            print("True")
        elif y % 100 == 0 and y % 400 != 0:
            print("False")
        elif y % 100 == 0 and y % 400 == 0:
            print("True")
    else:
        print("False")


leap_year(year)