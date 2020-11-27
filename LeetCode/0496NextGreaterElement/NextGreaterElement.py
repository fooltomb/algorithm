class Solution:
    def nextGreaterElement(self,nums1,nums2):
        res=[]
        for num in nums1:
            result=-1
            index=nums1.index(num2)
            
            for k in range(index,len(nums2)):
                if nums2[k]>num:
                    result=nums2[k]
                    break
            res.append(result)
        return res
