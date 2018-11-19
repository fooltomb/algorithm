#coding=utf-8
"""
the step reach n stairs is the step reach n-1 stairs and n-2 stairs
结果是斐波那契数列
但是结果还是会超时啊
"""
class Solution(object):
    def climbStairs(self,n):
        if n==1:
            return 1
        if n==2:
            return 2
        return self.climbStairs(n-1)+self.climbStairs(n-2)

if __name__=="__main__":
    s=Solution()
    print s.climbStairs(35)

