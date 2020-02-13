class Solution(object):
    def countPrimes(self,n):
        if n<3:
            return 0
        parms=[1]*n
        for i in range(2,int(n**0.5)+1):
            if parms[i]==1:
                for k in range(i*i,n,i):
                    parms[k]=0
        return sum(parms)-2

