class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            count=s.count(s[i])
            if(count==1):
                return i
        return -1

if __name__=="__main__":
    s=Solution()
    print(s.firstUniqChar("leetclde"))
