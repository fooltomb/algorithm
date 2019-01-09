class Solution(object):
    def firstBadVersion(self,n):
        flag=isBadVersion(n)
        cur=n
        while n//2>0:
            n=(n+1)//2
            if flag:
                cur-=n
            else:
                cur+=n
                
            flag=isBadVersion(cur)
        return cur if flag else cur+1

