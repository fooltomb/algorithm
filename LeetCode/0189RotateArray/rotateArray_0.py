class Solution(object):
    def rotate(self,nums,k):
        n=len(nums)
        k=k%n
        nums.reverse()
        for i in range(k/2):
            nums[i],nums[k-i-1]=nums[k-i-1],nums[i]
        for i in range((n-k)/2):
            nums[k+i],nums[n-i-1]=nums[n-i-1],nums[k+1]
