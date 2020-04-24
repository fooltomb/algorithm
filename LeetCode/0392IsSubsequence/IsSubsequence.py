class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if(len(s)==0):return True
        if(len(t)==0):return False
        i=0
        j=0
        while(i<len(s)):
            if(s[i]==t[j]):
                i+=1
                j+=1
            else:
                j+=1
            if(j==len(t)):
                if(i==len(s)):
                    return True
                return False
        return True
