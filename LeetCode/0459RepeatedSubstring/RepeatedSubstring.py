class Solution:
    def repeatedSubstringPattern(self, s) -> bool:
        max_n=len(s)//2
        for i in range(max_n,0,-1):
            if len(s)%i==0:
                flag=True
                for k in range((len(s)//i)-1):
                    if s[k*i:(k+1)*i]!=s[(k+1)*i:(k+2)*i]:
                        flag=False
                        break
                if flag==True:
                    return True
        return False

if __name__=="__main__":
    s=Solution()
    res=s.repeatedSubstringPattern("haaahaaahaaa")
    print(res)
