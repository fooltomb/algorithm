class Solution:
    def generateParenthesis(self, n: int) :
        self.count=n
        self.res=[]
        self.digui(0,0,"")
        return self.res
    def digui(self,opened,closed,t):
        if closed==self.count:
            self.res.append(t)
            return
        if opened==self.count:
            self.digui(opened,closed+1,t+")")
        elif opened==closed:
            self.digui(opened+1,closed,t+"(")
        else:
            self.digui(opened+1,closed,t+"(")
            self.digui(opened,closed+1,t+")")
            
if __name__=="__main__":
    s=Solution()
    r=s.generateParenthesis(0)
    print(r)
