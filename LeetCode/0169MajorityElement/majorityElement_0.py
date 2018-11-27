#Time Limit exceeded
'''
class Solution(object):
    def majorityElement(self,nums):
        count=len(nums)/2
        for num in nums:
            if nums.count(num)>count:
                return num
'''
class Solution(object):
    def majorityElement(self,nums):
        countDict={}
        cur=None
        for num in nums:
            if countDict.has_key(num):
                countDict[num]+=1
                if cur!=None:
                    if countDict[num]>countDict[cur]:
                        cur=num
                else:
                    cur = num
            else:
                countDict[num]=1
        return cur

if __name__=="__main__":
    s=Solution()
    print s.majorityElement([2,2,1,2])
