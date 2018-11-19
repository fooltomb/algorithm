class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution(object):
    def isSameTree(self,p,q):
        self.res=True
        self.isSame(p,q)
        return self.res
    def isSame(self,a,b):
        if a==None and b==None:
            return
        elif b==None or a==None:
            self.res=False
            return
        else:
            if a.val!=b.val:
                self.res=False
                return
            else:
                self.isSame(a.left,b.left)
                self.isSame(a.right,b.right)

