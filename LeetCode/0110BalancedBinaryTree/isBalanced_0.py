#coding:utf-8
#每个节点的左右节点长度之差不能大于1
class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
class Solution(object):
    def isBalanced(self,root):
        self.is_balance=True
        def DFS(rootNode):
            if not self.is_balance:
                return -2
            if(rootNode==None):
                return 0
            left=DFS(rootNode.left)
            right=DFS(rootNode.right)
            if abs(left-right)>1:
                self.is_balance=False
            return max(left,right)+1
        DFS(root)
        return self.is_balance

       
if __name__=="__main__":
    r=TreeNode(1)
    r.right=TreeNode(2)
    r.right.right=TreeNode(3)
    s=Solution()
    print s.isBalanced(r)
