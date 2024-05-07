class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        nums.sort()
        res=nums[0]+nums[1]+nums[2]
        for i in range(len(nums)-2):
            j,k=i+1,len(nums)-1
            while j<k:
                temp=nums[i]+nums[j]+nums[k]
                if temp>target:
                    k=k-1
                elif temp<target:
                    j=j+1
                else:
                    return temp
                if abs(temp-target)<abs(res-target):
                    res=temp
        return res


if __name__=="__main__":
    s=Solution()
    res=s.threeSumClosest([-1,2,1,-4,-1,2,1,-4],1)
    print(res)
