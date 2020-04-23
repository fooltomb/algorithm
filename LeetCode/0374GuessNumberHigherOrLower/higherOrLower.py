class Solution:
    def guessNumber(self, n: int) -> int:
        lower=1
        higher=n
        while(True):
            ans=lower+(higher-lower)//2
            ges=guess(ans)
            if(ges==0):
                return ans
            elif(ges<0):
                higher=ans-1
            else:
                lower=ans+1
