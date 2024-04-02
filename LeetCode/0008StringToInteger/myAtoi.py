class Solution:
    def myAtoi(self, s: str) -> int:
        res=0
        sign=1        
        for i in range(len(s)):
            t=s[i]
            if '0'<=t and t<='9':
                res=res*10+int(t)*sign
                flag=True
            elif t=='-':
                sign=-1
            elif t=='+':
                sign=1
            elif t==' ':
                continue
            else:
                break
        if res<-2147483648:
            return -2147483648
        if res>2147483647:
            return 2147483647
        return res


if __name__=="__main__":
    s=Solution()
    print(s.myAtoi("+-12"))
