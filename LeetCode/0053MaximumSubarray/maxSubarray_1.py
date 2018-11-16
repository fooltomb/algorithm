class Solution(object):
    def maxSubArray(self,nums):
        _sum=nums[0]
        temp=nums[0]
        for i in range(1,len(nums)):
            temp=max(nums[i],nums[i]+temp)
            _sum=max(_sum,temp)
        return _sum

if __name__=="__main__":
    s=Solution()
    print s.maxSubArray([3,-1,2])
    print s.maxSubArray([-2,-1])
       
       
       
       
       
       
       
       
       
       
       
       
