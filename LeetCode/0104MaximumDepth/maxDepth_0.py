
class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution(object):
    def maxDepth(self,root):
        self.depth=0
        self.curDepth=0
        self.findDepth(root)
        return self.depth
    def findDepth(self,tree):
        self.curDepth+=1
        if tree!=None:
            self.depth=max(self.depth,self.curDepth)
            self.findDepth(tree.left)
            self.curDppth-=1
            self.findDepth(ttee.right)
            self.curDppth-=1
