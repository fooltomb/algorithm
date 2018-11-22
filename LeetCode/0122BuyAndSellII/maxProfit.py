class Solution(object):
    def maxProfit(self,prices):
        if prices==[]:
            return 0
        res=0
        for i in range(1,len(prices)):
            res+=max(0,prices[i]-prices[i-1])
        return res

