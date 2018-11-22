class Solution(object):
    def generate(self,numRows):
        if numRows==0:
            return []
        res=[[1]]
        for i in range(1,numRows):
            cur=[1]
            for k in range(i):
                if k==i-1:
                    cur.append(1)
                else:
                    cur.append(res[i-1][k+1]+res[i-1][k])
            res.append(cur)
        return res
    



