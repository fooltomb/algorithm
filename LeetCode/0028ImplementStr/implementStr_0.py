class Solution(object):
    def strStr(self,haystack,needle):
        return haystack.find(needle)

if __name__=="__main__":
    s=Solution()
    print s.strStr("needle","ae")
