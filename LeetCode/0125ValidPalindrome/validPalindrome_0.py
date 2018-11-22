class Solution(object):
    def isPalindrome(self,s):
        res=""
        for char in s.lower():
            if char.isalnum():
                res+=char
        print res
        if res==res[::-1]:
            return True
        else:
            return False
if __name__=="__main__":
    s=Solution()
    print s.isPalindrome("raFce a car")
