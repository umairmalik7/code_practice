class Solution:
    def findAnswer(self, d, n): 
       #Code here
        days = ["sunday","Monday","Tuesday","Wednesday","Thursday","Friday","saturday"]
        actual_day = (d - n ) % 7
        day2 = days[actual_day]
        index = days.index(day2)
        return index
       
       
        
