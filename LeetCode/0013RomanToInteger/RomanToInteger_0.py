class Solution(object):
    def romanToInt(self,s):
        """
        """
        dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        res=dict[s[-1]]
        for i in range(-1,-len(s),-1):
            if dict[s[i-1]]>=dict[s[i]]:
                res+=dict[s[i-1]]
            else:
                res-=dict[s[i-1]]
        return res

if __name__=="__main__":
    s=Solution()
    print s.romanToInt("LVIII")
    print s.romanToInt("MCMXCIV")

