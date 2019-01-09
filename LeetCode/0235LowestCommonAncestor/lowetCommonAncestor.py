# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.stack=[]
        self.getStack(root,p)
        while True:
            res=self.stack.pop()
            if self.getQ(res,q):
                return res
        
    def getStack(self,root,p):
        self.stack.append(root)
        if root==None:
            return False
        if root==p:
            return True   
        if self.getStack(root.left,p):
            return True
        else:
            self.stack.pop()
            if self.getStack(root.right,p):
                return True
            else:
                self.stack.pop()
                return False
    def getQ(self,root,q):
        if root==None:
            return False
        if root==q:
            return True
        if self.getQ(root.left,q):
            return True
        else:
            return self.getQ(root.right,q)