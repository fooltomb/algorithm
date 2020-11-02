class Solution:
    def findContentChildren(self, g, s) -> int:
        g.sort()
        s.sort()
        i=0
        j=0
        res=0
        while i<len(g) and j<len(s):
            if s[j]>=g[i]:
                res+=1
                i+=1
                j+=1
            else:
                j+=1
        return res

if __name__=="__main__":
    s=Solution()
    res=s.findContentChildren([1,2,3],[2,2,2])
    print(res)
