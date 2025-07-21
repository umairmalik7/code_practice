class Solution:
    def checkStatus(self, a, b, flag):
        # code here
        if a < 0 and b > 0 or b < 0 and a > 0:
            if flag is False:
                return True
            elif flag is True:
                return False
           
        elif a < 0 and b < 0 :
            if flag == False:
                return False
            elif flag is True:
                return True
        else:
            return False