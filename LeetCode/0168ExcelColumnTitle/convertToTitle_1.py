class Solution(object):
    def convertToTitle(self,n):
        if n==0:
            return ""
        else:
            return self.convertToTitle((n-1)//26)+chr((n-1)%26+ord('A'))
        
