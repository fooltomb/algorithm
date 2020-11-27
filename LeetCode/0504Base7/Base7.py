class Solution:
    def convertToBase7(self,num):
        flag=""
        
        c=num
        if(num==0):return "0"
        if(num<0):
            flag="-"
            c=c*-1
        result=[flag]
        while(c>0):
            result.insert(1,str(c%7))
            c=c//7
        
        return "".join(result)
