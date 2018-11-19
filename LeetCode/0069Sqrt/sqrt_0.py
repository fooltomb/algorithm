#newton's method
class Solution(object):
    def mySqrt(self,x):
        k=1
        while True:
            p=k
            k=(k+x/k)/2
            if(p==k):
                print k
                break
        return int(k)

if __name__=="__main__":
    s=Solution()
    print s.mySqrt(1500)
