class Solution(object):
    def searchInsert(self,nums,target):
        for i in range(len(nums)):
            if nums[i]>=target:
                return i
        return len(nums)

if __name__=="__main__":
    s=Solution()
    print s.searchInsert([1,2,4,5,7],6)
