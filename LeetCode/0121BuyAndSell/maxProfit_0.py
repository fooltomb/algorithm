class Solution(object):
    def maxProfit(self,prices):
        if prices==[]:
            return 0
        lower=prices[0]
        res=0
        for i in range(len(prices)):
            lower=min(lower,prices[i])
            res=max(res,prices[i]-lower)
        return res
    
if __name__=="__main__":
    s=Solution()
    print s.maxProfit([3,1,2,3,1])

