class Solution(object):
    def longestCommonPrefix(self,strs):
        """
        """
        prefix=strs[0]
        for i in range(1,len(strs)):
            while strs[i].find(prefix)==-1:
                prefix=prefix[0:-1]
                if prefix=="":
                    return ""
        return prefix

if __name__=="__main__":
    s=Solution()
    print s.longestCommonPrefix(["leets","leetcode","leo"])

