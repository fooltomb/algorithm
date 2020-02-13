class Solution(object):
    def missingNumber(self,nums):
        n=len(nums)
        su=(n+1)*n/2
        return su-sum(nums)

