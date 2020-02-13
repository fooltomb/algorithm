class Solution(object):
    def isPowerOfFour(self,num):
        if num<1:
            return False
        twoBase=bin(num)
        n=len(twoBase)
        if n%2==0:
            return False
        for i in twoBase[3:]:
            if i!='0':
                return False
        return True

