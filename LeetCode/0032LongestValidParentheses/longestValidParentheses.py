class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res=0
        cnt=0
        length=0
        index=0
        for i in range(len(s)):
            if s[i]=="(":
                cnt+=1
            else:
                cnt-=1
                length+=2            
            if cnt<0:
                res=max(res,length-2)
                cnt=0
                length=0
                index=i+1
        if cnt==0:
            return max(res,length)
        res1=0
        cnt=0
        length=0
        for i in range(len(s)-1,index-1,-1):
            print("i"+str(i))
            if s[i]==")":
                cnt+=1
            else:
                cnt-=1
                length+=2            
            if cnt<0:
                res1=max(res1,length-2)
                cnt=0
                length=0
        return max(res,res1,length)




if __name__=="__main__":
    s=Solution()
    r=s.longestValidParentheses("()")
    print(r)
