class Solution(object):
    def hasPathSum(self,root,sum):
        if root==None:
            return False
        self.has=False
        def DFS(curNode):
            if self.has:
                return
            if curNode.val==sum and curNode.left==None and curNode.right==None:
                self.has=True
                return
            if curNode.left!=None:
                curNode.left.val+=curNode.val
                DFS(curNode.left)
            if curNode.right!=None:
                curNode.right.val+=curNode.val
                DFS(curNode.right)
        DFS(root)
        return self.has

