class Solution(object):
    def climbStairs(self,n):
        if n==1:return 1
        if n==2:return 2
        oneForward=2
        twoForward=1
        allstep=0

        for i in range(2,n):
            #oneForward=oneForward+twoForward
            #twoForward=oneForward
            allstep=oneForward+twoForward
            twoForward=oneForward
            oneForward=allstep
        return allstep

if __name__=="__main__":
    s=Solution()
    print s.climbStairs(35)
