class Solution:
    def minMoves(self, nums) -> int:
        nums.sort()
        res=0
        for i in range(len(nums)-1):
            res=res+nums[i+1]-nums[0]
        return res

if __name__=="__main__":
    s=Solution()
    res=s.minMoves([1,2,2,3])
    print(res)

