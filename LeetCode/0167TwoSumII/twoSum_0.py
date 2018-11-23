class Solution(object):
    def twoSum(self,numbers,target):
        index1=0
        index2=1
        while numbers[index1]+numbers[index2]!=target:
            if numbers[index1]+numbers[index2]<target:
                index1+=1
                index2+=1
            
            elif numbers[index1]+numbers[index2]>target:
                index1-=1
        return [index1,index2]

if __name__=="__main__":
    s=Solution()
    print s.twoSum([1,2,3,4,5,6],4)




