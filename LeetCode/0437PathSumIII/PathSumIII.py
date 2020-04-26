# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.target=sum
        self.res=0
        self.nodeSum=[]
        self.getRes(root)
        return self.res
    def getRes(self,node:TreeNode):
        if node==None:return
        if node.val==self.target:
            self.res+=1
        for i in range(len(self.nodeSum)):
            self.nodeSum[i]+=node.val
            if self.nodeSum[i]==self.target:
                self.res+=1
        self.nodeSum.append(node.val)
        self.getRes(node.left)
        self.getRes(node.right)
        del self.nodeSum[-1]
        for i in range(len(self.nodeSum)):
            self.nodeSum[i]-=node.val
