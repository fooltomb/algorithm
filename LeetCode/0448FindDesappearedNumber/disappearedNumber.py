class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[]
        for num in nums:
            nums[abs(num)]=-abs(nums[abs(num)])
        for i in range(n):
            if nums[i]>0:
                res.append(i)
        return res
