class Solution:
    def countBits(self,n:int)->list[int]:
        res=[0]
        a=1
        for i in range(1,n+1):
            if i>=2*a:
                a=a*2
            res.append(1+res[i-a])
            print(a,i)
        return res

if __name__=="__main__":
    su=Solution()
    print(su.countBits(16))

                
