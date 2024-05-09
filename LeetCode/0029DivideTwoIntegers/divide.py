class Solution:
    def divide(self, dividend: int, divisor: int) -> int:        
        reverse=False
        if dividend>0 and divisor>0:
            dividend=-dividend
            divisor=-divisor
        elif dividend>0:
            dividend=-dividend
            reverse=True
        elif divisor>0:
            divisor=-divisor
            reverse=True
        self.divisor=divisor           
        res=self.div(dividend)
        if reverse:
            return -res
        else:
            return res

    def div(self,dividend):
        divisor=self.divisor
        res=0
        if dividend<=divisor:
            res=1
        else:
            return 0
        while True:
            b=divisor+divisor
            if dividend<=b:
                res=res+res
                divisor=b
                #print(divisor)
            else:
                break
        return res+self.div(dividend-divisor)


if __name__=="__main__":
    s=Solution()
    r=s.divide(-2,2)
    print(r)
