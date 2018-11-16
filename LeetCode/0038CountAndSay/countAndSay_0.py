class Solution(object):
    def countAndSay(self,n):
        s="1"
        for i in range(n-1):
            res=""
            count=0
            curstr=s[0]
            for k in range(len(s)):
                if s[k]==curstr:
                    count+=1
                else:
                    res+=str(count)+curstr
                    curstr=s[k]
                    count=1
            res+=str(count)+curstr
            s=res
            #print s
        return s

if __name__=="__main__":
    sol=Solution()
    print sol.countAndSay(7)
