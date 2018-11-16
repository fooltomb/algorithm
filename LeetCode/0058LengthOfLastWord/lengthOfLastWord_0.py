class Solution(object):
    def lengthOfLastWord(self,s):
        s=s.stirp()
        index=s.rfind(' ')
        return len(s)-index-1

if __name__=="__main__":
    s=Solution()
    print s.lengthOfLastWord("w")
