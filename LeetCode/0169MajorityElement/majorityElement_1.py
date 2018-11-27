#coding:utf-8
#因为主要元素的个数大于n/2,所以比其它所有元素的和都大
class Solution(object):
    def majorityElement(self,nums):
        major=nums[0]
        count=1
        for num in nums:
            if(count==0):
                count++1
                major=num
            elif major==num:
                count+=1
            else:
                count-=1
        return major
if __name__=="__main__":
    s=Solution()
    print s.majorityElement([2,1,3,3,3])
