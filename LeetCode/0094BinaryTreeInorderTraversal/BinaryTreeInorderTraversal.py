class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        if root==None:
            return []
        res=[]
        res=it(root,res)
        return res


def it(node,res)->int:
    if node.left!=None:
        res=it(node.left,res)
    res.append(node.val)
    if node.right!=None:
        res=it(node.right,res)
    return res

if __name__=="__main__":
    t=TreeNode(3);
    t=TreeNode(2,t,None)
    t=TreeNode(1,None,t)
    su=Solution()
    print(su.inorderTraversal(t))
