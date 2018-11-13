class Solution(object):
    def twoSum(self,nums,target):
        """
        """
        for i in range(len(nums)):
            for k in range(i+1,len(nums)):
                if nums[i]+nums[k]==target:
                    return [i,k]

if __name__=="__main__":
    s=Solution()
    a=s.twoSum([4,4,3,5],8)
    print a
    
