class Solution(object):
    def isUgly(self,num):
        if num<=0:
            return False
        if num==1:
            return True
        def DFS(num):
            if num==2 or num==3 or num==5:
                return True
            if num%2==0:
                return DFS(num/2)
            elif num%3==0:
                return DFS(num/3)
            elif num%5==0:
                return DFS(num/5)
            else:
                return False
        return DFS(num)
