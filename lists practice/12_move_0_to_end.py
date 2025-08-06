class Solution:
	def pushZerosToEnd(self,arr):
    	# code here
    	
        mylist = []
        for i in range(len(arr)):
            if arr[i] != 0:
                mylist.append(arr[i])
        for i in range(len(arr)-len(mylist)):
            mylist.append(0)
         
        for i in range(len(arr)):
            arr[i] = mylist[i]
    
        return arr