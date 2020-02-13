class Solution(object):
    def isHappy(self,n):
        done=[n]
        while(n!=1):
            n=self.cycle(n)
            try:
                done.index(n)
                break
            except:
                done.append(n)
                continue
        return True if n==1 else False
    def cycle(self,n):
        s=0
        num=str(n)
        for i in range(len(num)):
            s+=int(num[i])**2
        return s
