class Solution(object):
    def containDuplicate(self,nums):
        a=len(nums)
        b=len(set(nums))
        return a>b
