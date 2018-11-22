class Solution(object):
    def getRow(self,rowIndex):
        res=[1]
        if rowIndex==0:
            return res
        for i in range(rowIndex):
            res.append(1)
            for k in range(-2,-len(res),-1):
                res[k]+=res[k-1]
        return res

if __name__=="__main__":
    s=Solution()
    print s.getRow(1)
