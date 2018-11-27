class Solution(object):
    def titleToNumber(self,s):
        mul=1
        su=0
        for i in range(-1,-len(s)-1,-1):
            su+=(ord(s[i])-64)*mul
            mul*=26
        return su

if __name__=="__main__":
    s=Solution()
    print s.titleToNumber("ZY")

