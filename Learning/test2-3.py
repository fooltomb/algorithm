class Solution:
    def triangle(self,n):
        '''
        输出n层倒三角n<21
        '''
        for i in range(n,0,-1):
            s=""
            for j in range(n-i):
                s+=' '
            for k in range(i*2-1):
                s+='#'
            print (s)

if __name__=="__main__":
    s=Solution()
    s.triangle(3)