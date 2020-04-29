class Solution:
    def arrangeCoins(self, n: int) -> int:
        res=0
        left=n
        rowOfCoins=0
        while (left>0):
            rowOfCoins+=0
            left-=rowOfCoins
            if(left>=0):
                res+=1
        return res
#k*(k+1)=2n result=(sqrt(1+8n)-1)/2
