class Solution(object):
    def addDigits(self,num):
        #如果num==100a+10b+c,那么(100a+10b+c)%9==(99a+a+9b+b+c)%9==(a+b+c)%9
        if num==0 return 0
        return 9 if num%9==0 else num%9
