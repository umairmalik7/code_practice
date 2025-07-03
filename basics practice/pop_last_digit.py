class Solution:
    def lastDigit(self, n: int) -> int:
        #Code here
        string = str(n)
        list = [x for x in string ]
        last_digit = list.pop()
        return last_digit
        