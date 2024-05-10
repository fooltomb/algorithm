class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        def findandsort(a,l):
            index=-1
            cur=101
            for i in range(len(l)):
                if l[i]>a and l[i]<cur:
                    cur=l[i]
                    index=i
            if index!=-1:
                l[index]=a
                l.sort()
                return True,cur,l
            else:
                return False,0,[]
        flag=False
        for i in range(len(nums)-2,-1,-1):
            flag,cur,tail=findandsort(nums[i],nums[i+1:])
            if flag:
                nums[i]=cur
                nums[i+1:]=tail
                break
        if not flag:
            nums.sort()
        print(nums)

if __name__=="__main__":
    s=Solution()
    r=s.nextPermutation([3, 4, 1, 2])
    r=s.nextPermutation([3, 4, 2, 1])
    r=s.nextPermutation([4,1,2,3])
    r=s.nextPermutation([4,3,2,1])
    #print(r)

            
