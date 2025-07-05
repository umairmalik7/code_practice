day = int(input("day: "))
num = int(input("num: "))
def findAnswer( d, n): 
       #Code here
    days = ["sunday","Monday","Tuesday","Wednesday","Thursday","Friday","saturday"]
    actual_day = (d - n ) % 7
    print(f"{d} -{n} % 7 =", actual_day)
    day2 = days[actual_day]
    index = days.index(day2)
    return index
       
       
findAnswer(day, num)
        
