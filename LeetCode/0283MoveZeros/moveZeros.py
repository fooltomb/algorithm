class Solution(object):
    def moveZeros(self,nums):
        k=0
        for i in range(len(nums)):
            if k<len(nums):
                while k<len(nums)-1 and nums[]==0:
                    k+=1
                nums[i]=nums[k]
                k+=1
            else:
                nums[i]=0

