class Solution(object):
    def merge(self,nums1,m,nums2,n):
        while m>0 and n>0:
            if nums1[m-1]>=nums2[n-1]:
                nums1[m+n-1]=nums1[m-1]
                m-=1
            else:
                nums1[m+n-1]=nums2[n-1]
                n-=1
        if m==0:
            nums1[:n]=nums2[:n]
        print nums1
if __name__=="__main__":
    s=Solution()
    nums=[1,2,4,5,0,0,0]
    numss=[3,3,6]
    s.merge(nums,4,numss,3)


