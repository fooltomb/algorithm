class Solution(object):
    def removeDuplicates(self,nums):
        if len(nums)==0:
            return 0
        length=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[length]=nums[i]
                length+=1
        return length

if __name__=="__main__":
    s=Solution()
    n=[2,2,2,3,3,3,4,4,5,5]
    print s.removeDuplicates(n)
    print n

