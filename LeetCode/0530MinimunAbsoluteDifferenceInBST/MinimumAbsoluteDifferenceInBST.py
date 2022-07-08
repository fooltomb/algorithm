class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution:
    def getMinimumDifference(self,root):
        self.tempMin=2**31
        self.getMin(root)
        return self.tempMin
    def getMin(self,node):
        if(node.left!=None):
            self.tempMin=min(self.tempMin,abs(node.val-self.getLeftMin(node.left)))
        if(node.right!=None):
            self.tempMin=min(self.tempMin,abs(node.val-self.getRightMin(node.right)))
        if(node.left!=None):self.getMin(node.left)
        if(node.right!=None):self.getMin(node.right)
        
    def getLeftMin(self,node):
        if(node.right!=None):
            return self.getLeftMin(node.right)
        else:
            return node.val
        
    def getRightMin(self,node):
        if(node.left!=None):
            return self.getRightMin(node.left)
        else:
            return node.val
