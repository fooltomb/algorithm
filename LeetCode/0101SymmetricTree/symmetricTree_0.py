#vim: set fileencoding:utf-8
#逐层遍历存到一个数组里，然后把数组翻过来看看一样否
#Definition for a binary tree node
class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution(object):
    def isSymmetric(self,root):
        stack=[root]#这只是个列表不是栈
        while len(stack)>0:
            #对当前层，把每个节点的左右孩放进列表，并删除父节点
            for i in range(len(stack)):
                if(stack[0]!=None):
                    stack.append(stack[0].left)
                    stack.append(stack[0].right)
                stack=stack[1:]
            res=[]
            for i in range(len(stack)):
                if stack[i]!=None:
                    res.append(stack[i].val)
                else:
                    res.append(None)
            if res!=res[::-1]:
                return False
        return True
if __name__=="__main__":
    a=TreeNode(1)
    a.left=TreeNode(2)
    a.right=TreeNode(2)
    a.left.left=TreeNode(3)
    s=Solution()
    print s.isSymmetric(a)


