class Solution:
    def findRelativeRanks(self,nums):
        result=[1]*len(nums)
        for i in range(len(nums)):
            for k in range(i,len(nums)):
                if nums[i]>nums[k]:
                    result[k]+=1
                else:
                    result[i]+=1
        for i in range(len(result)):
            if result[i]==1:
                result[i]="Gold Medal"
            elif result[i]==2:
                result[i]="Silver Medal"
            elif result[i]==3:
                result[i]="Bronze Medal"
            else:
                result[i]=str(result[i])
        return result
