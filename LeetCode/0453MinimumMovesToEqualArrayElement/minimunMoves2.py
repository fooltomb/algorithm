class Solution:
    def minMoves(self, nums) -> int:
        cur_min=nums[0]
        res=0
        for i in range(len(nums)):
            if nums[i]==cur_min:
                continue
            elif nums[i]>cur_min:
                res+=nums[i]-cur_min
            else:
                res+=i*(cur_min-nums[i])
                cur_min=nums[i]
    
        return res

if __name__=="__main__":
    s=Solution()
    res=s.minMoves([3,2,2,-1])
    print(res)

