#Time Limit Exceeded:wq

class Solution(object):
    way=0
    def climbStairs(self,n):
        self.DFS(n)
        return self.way
    def DFS(self,remainStep):
        if remainStep-1==0:
            self.way+=1
            return
        elif remainStep-2==0:
            self.way+=2
            return
        else:
            self.DFS(remainStep-1)
            self.DFS(remainStep-2)

if __name__=="__main__":
    s=Solution()
    print s.climbStairs(30)

