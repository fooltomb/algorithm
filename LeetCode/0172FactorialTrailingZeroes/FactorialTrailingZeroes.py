class Solution(object):
    def trailingZeroes(self,n):
        su=0
        tag=5
        while(n>=tag):
            su+=n/tag
            tag*=5
        return su
