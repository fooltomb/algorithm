class Solution:
    def thirdMax(self, nums) -> int:
        res=[nums[0]]
        for num in nums:
            if(len(res)==3):
                if num==res[0] or num==res[1] or num==res[2]:
                    continue
                if num>res[0]:
                    res[2]=res[1]
                    res[1]=res[0]
                    res[0]=num
                elif num>res[1]:
                    res[2]=res[1]
                    res[1]=num
                elif num>res[2]:
                    res[2]=num
            if(len(res)==2):
                if num==res[0] or num==res[1]:
                    continue
                if num>res[0]:
                    res.append(res[1])
                    res[1]=res[0]
                    res[0]=num
                elif num>res[1]:
                    res.append(res[1])
                    res[1]=num
                else:
                    res.append(num)
            if(len(res)==1):
                if num==res[0]:
                    continue
                if num>res[0]:
                    res.append(res[0])
                    res[0]=num
                else:
                    res.append(num)
                
        if len(res)==3:
            return res[2]
        else:
            return res[0]

if __name__=="__main__":
    s=Solution()
    print(s.thirdMax([1,3,-382038]))
