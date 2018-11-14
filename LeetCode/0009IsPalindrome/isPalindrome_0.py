class Solution(object):
    def isPalindrome(self,x):
        s=str(x)
        rs=s[::-1]
        return True if s==rs else False

if __name__=="__main__":
    s=Solution()
    print s.isPalindrome(93939)

    print s.isPalindrome(-93939)
