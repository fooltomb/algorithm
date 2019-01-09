class Solution(object):
    def wordPattern(self,pattern,str):
        resP={}
        resS={}
        strs=str.split()
        if len(pattern)!=len(strs):
            return False
        for i in range(len(strs)):
            if resP.has_key(pattern[i]):
                if resP[pattern[i]]!=strs[i]:
                    return False
            else:
                resP[pattern[i]]=strs[i]
            if resS.has_key(strs[i]):
                if resS[strs[i]]!=pattern[i]:
                    return False
            else:
                resS[strs[i]]=pattern[i]
        return True

