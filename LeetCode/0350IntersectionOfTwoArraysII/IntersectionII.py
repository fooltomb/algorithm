class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #sort arrays to be able to use 2-pointer solution
        nums1.sort()
        nums2.sort()
    
        i1 = 0
        i2 = 0
        
        ans = []
        
        #increment the pointer of the array which current element is smaller
        while i1 < len(nums1) and i2 < len(nums2): 
            if nums1[i1] == nums2[i2]:
                ans.append(nums1[i1])
                i1+=1
                i2+=1 
            elif nums1[i1] < nums2[i2]:
                i1+=1
            else:
                i2+=1
                
        return ans
