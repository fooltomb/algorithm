class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        l=len(s)
        reverse=""
        for i in range(0,l,2*k):
            reverse+=self.reverse(s[i:i+k])
            reverse+=s[i+k:i+2*k]
        return reverse

    def reverse(self,s:str):
        res=""
        for i in range(len(s),0,-1):
            res = res +s[i-1]
        return res

if __name__=="__main__":
    so=Solution()
    print(so.reverseStr("abcdefghij",3))


