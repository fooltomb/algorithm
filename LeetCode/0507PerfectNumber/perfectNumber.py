class Solution:
    def checkPerfectNumber(self,num):
        res=1
        i=2
        end=num
        while i<end:
            if num%i==0:                
                res+=i+end
            end=num/i
            print("end:")
            print(end)
            print(i)
            i+=1
        return res==num

if __name__=="__main__":
    s=Solution()
    print(s.checkPerfectNumber(28))
