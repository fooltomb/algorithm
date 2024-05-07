class Solution:
    def fourSum(self, nums, target: int):
        nums.sort()
        res=[]
        for i in range(len(nums)-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,len(nums)-2):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                k,l=j+1,len(nums)-1
                while k<l:
                    temp=nums[i]+nums[j]+nums[k]+nums[l]
                    if temp>target:
                        l=l-1
                    elif temp<target:
                        k=k+1
                    else:
                        res.append([nums[i],nums[j],nums[k],nums[l]])
                        l=l-1
                        k=k+1
                        while nums[l]==nums[l+1] and k<l:
                            l=l-1
                        while nums[k]==nums[k-1] and k<l:
                            k=k+1
        return res

if __name__=="__main__":
    s=Solution()
    r=s.fourSum([-2,-1,-1,1,1,2,2],0)
    print(r)
