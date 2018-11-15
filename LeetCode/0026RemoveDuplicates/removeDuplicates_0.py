class Solution(object):
    def removeDuplicates(self,nums):
        if len(num)==0:
            return 0
        index=0
        while True:
            if index==len(nums)-1:
                break
            if nums[index]==nums[index+1]:
                nums.remove(nums[index])
            else:
                index+=1

        return len(nums)
if __name__=="__main__":
    s=Solution()
    n=[0,0,0,1,2,3,3,3,4,5]
    print len(n)
    print s.removeDuplicates(n)
    print n







