class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution(object):
    def levelOrderBottom(self,root):
        if root==None:
            return []
        stack=[root]
        result=[[root.val]]
        while len(stack)>0:
            for i in range(len(stack)):
                if stack[0]!=None:
                    stack.append(stack[0].left)
                    stack.append(stack[0].right)
                stack=stack[1:]
            res=[]
            for tree in stack:
                if tree!=None:
                    res.append(tree.val)
            if res!=[]:
                result.insert(0,res[:])
        return result
