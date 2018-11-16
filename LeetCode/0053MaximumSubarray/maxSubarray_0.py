#这个解法会超时
class Solution(object):
    def maxSubArray(self,nums):
        _sum=nums[0]
        for i in range(len(nums)):
            for k in range(i+1,len(nums)+1):
                temp=0
                for num in nums[i:k]:
                    temp+=num
                if temp>_sum:
                    _sum=temp

        return _sum

if __name__=="__main__":
    s=Solution()
    print s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])

    print s.maxSubArray([-2,-1])
    print [-2,2][1:2]
