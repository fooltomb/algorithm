class Solution:
    def hammingDistance(self,x,y)->int:
        p=x^y
        bp=bin(p)
        sum=0
        for i in range(2,len(bp)):
            sum+=int(bp[i])
        return sum

if __name__=="__main__":
    s=Solution()
    res=s.hammingDistance(1,3)
    print(res)
