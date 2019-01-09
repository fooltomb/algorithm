# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res=[]
        stack=[]
        def DFS(root):
            stack.append(root)
            if root==None:
                return
            if root.left==None and root.right==None:
                AddToRes()
                return
            DFS(root.left)
            stack.pop()
            DFS(root.right)
            stack.pop()
        def AddToRes():
            s=""
            for node in stack:
                s+=str(node.val)
                s+="->"
            res.append(s[:-2])
        DFS(root)
        return res