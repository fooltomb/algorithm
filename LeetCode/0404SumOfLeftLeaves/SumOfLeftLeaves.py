# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if(root==None):return 0
        self.sum=0
        self.getLeft(root,False)
        return self.sum
    def getLeft(self,node:TreeNode,isLeft:bool):
        if(node.left==None and node.right==None and isLeft):
            self.sum+=node.val
            return
        if(node.left!=None):
            self.getLeft(node.left,True)
        if(node.right!=None):
            self.getLeft(node.right,False)
            
