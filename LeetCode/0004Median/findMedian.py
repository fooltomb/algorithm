# -*- coding:utf-8 -*-
class Solution(object):
    def findMedianSortedArrays(self,nums1,nums2):
        
        m=len(nums1)
        n=len(nums2)
        if m==0:
            return self.getMedian(nums2)
        if n==0:
            return self.getMedian(nums1)

        i=0
        j=0
        cur=(nums1[0],nums2[0])
        while True:
            if(nums1[i]>nums2[j]):
                cur=nums2[j]
                j=j+1                
            else:
                cur=nums1[i]
                i=i+1
            if i+j>=(n+m)/2.0:
                if(n+m)%2!=0:
                    return cur
                else:
                    if(i==m):
                        return (cur+nums2[j])/2.0
                    if(j==n):
                        return (cur+nums1[i])/2.0
                    return (cur+min(nums1[i],nums2[j]))/2.0
            if i==m:
                if(n+m)%2==0:
                    return (nums2[(n-m)/2]+nums2[(n-m)/2-1])/2.0
                else:
                    return nums2[(n-m)/2]
            if j==n:
                if(n+m)%2==0:
                    return (nums1[(m-n)/2]+nums1[(m-n)/2-1])/2.0
                else:
                    return nums1[(m-n)/2]
                    


    def getMedian(self,nums):
        length=len(nums)
        if length%2==0:
            return (nums[length/2]+nums[length/2-1])/2.0
        else:
            return nums[length//2]


if __name__=="__main__":
    s=Solution()
    res=s.findMedianSortedArrays([],[2,3])
    print(res)
