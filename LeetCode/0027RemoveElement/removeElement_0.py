class Solution(object):
    def removeElement(self,nums,val):
        if len(nums)==0:
            return 0
        index=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[i],nums[index]=nums[index],nums[i]
                index+=1
        return index
if __name__=="__main__":
    s=Solution()
    n=[4,6,3,9,9,9,6,9]
    print s.removeElement(n,9)
    print n
