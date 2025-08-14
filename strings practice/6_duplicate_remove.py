#User function Template for python3
class Solution:

	
	def removeDuplicates(self, s):
	    # code here
	    a = []
        for i in s:
            if i not in a:
                a.append(i)
            
        newstr = "".join(a)
        return newstr