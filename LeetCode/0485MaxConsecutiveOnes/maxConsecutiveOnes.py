class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res=0
        tmp=0
        for num in nums:
            if num==0:
                res=max(res,tmp)
                tmp=0
            else:
                tmp+=1
        res=max(res,tmp)
        return res
