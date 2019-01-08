class Solution(object):
    def isIsomorphic(self,s,t):
        dictStoT={}
        dictTtoS={}
        for i in range(len(s)):
            if dictStoT.has_key(s[i]) and dictStoT[s[i]]!=t[i] or dictTtoS.has_key(t[i]) and dictTtoS[t[t]]!=s[i]:
                return False
            else:
                dictStoT[s[i]]=t[i]
                dictTtoS[t[i]]=s[i]
        return True

