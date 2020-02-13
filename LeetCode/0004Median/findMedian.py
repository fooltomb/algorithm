# -*- coding:utf-8 -*-
class Solution(object):
    def findMedianSortedArrays(self,nums1,nums2):
        if len(nums1)==0:
            return self.getMedian(nums2)
        if len(nums2)==0:
            return self.getMedian(nums1)

        if nums1[0]>nums2[0]:
            self.newlist=nums2.extend(nums1)
        else:
            self.newlist=nums1.extend(nums2)
    def getMedian(self,nums):
        length=len(nums)
        if length%2==0:
            return (nums[length/2]+nums[length/2-1])/2.0
        else:
            return nums[length//2]
    def med(self,longnum,shortnum):
        m=len(longnum)
        n=len(shortnum)
        medianLong=longnum[m//2]
        index=n//2
        if shortnum[0]>=medianLong:
            index=0
        elif shortnum[-1]<=medianLong:
            index=n
        else:
            half=index
            while not shortnum[index]<=medianLong<shortnum[index+1]:
                if medianLong<shortnum[index]:
                    index-=half//2
                else:
                    index+=half//2
                half=half//2
                if half==0:
                    index-=1
                    break
        print index#index在小的那边

if __name__=="__main__":
    s=Solution()
    s.med([1,3,5,8,10],[1,2,6])
