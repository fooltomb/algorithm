class Solution:
    def subsequence(self,n,m):
        s=0
        for i in range(n,m+1):
            s+=1.0/(i*i)
        print("%.4f"%s)

if __name__=="__main__":
    s=Solution()
    s.subsequence(2,4)