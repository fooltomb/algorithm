class Solution(object):
    def intersection(self,nums1,nums2):
        a=set(nums1)
        b=set(nums2)
        ab=a&b
        return list(ab)

