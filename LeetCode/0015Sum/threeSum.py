class Solution:
    def threeSum(self, nums):
        nums=sorted(nums)
        res=[]
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1,len(nums)):
                    if nums[i]+nums[j]+nums[k]==0:
                        res.append([nums[i],nums[j],nums[k]])
        return res

if __name__=="__main__":
    s=Solution()
    print(s.threeSum([-1,0,1,2,-1,-4]))
