class Solution(object):
    def isAnagram(self,s,t):
        if len(s)!=len(t):
            return False
        counter=[0]*26
        for i in range(len(s)):
            counter[ord(s[i])-97]+=1
        for i in range(len(t)):
            counter[ord(t[i])-97]-=1
        for count in counter:
            if count!=0:
                return False
        return True

