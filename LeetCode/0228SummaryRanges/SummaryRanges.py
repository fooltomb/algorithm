class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        res=[]
        i=0
        n=len(nums)
        while i<n:
            s=[nums[i]]
            for j in range(i+1,n):                
                if nums[j]==s[-1]+1:
                    s.append(nums[j])                
                else:                
                    break
            if(len(s)==1):
                res.append(str(s[0]))
            else:
                res.append(str(s[0])+"->"+str(s[-1]))
            i=i+len(s)
            
        return res

if __name__=="__main__":
    su=Solution()
    print(su.summaryRanges([0,2,3,4,6,7,8,12]))
