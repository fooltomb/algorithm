class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Stack:
    def __init__(self,top):
        self.top=TreeNode(val=top)
        self.depth=1
    def push(self,node):
        self.depth+=1
        self.top=TreeNode(val=node,left=self.top)
    def pop(self):
        if self.top==None:
            return None
        res=self.top 
        self.top=self.top.left
        self.depth-=1
        return res

class Solution:
    def countNodes(self, root) -> int:
        if(root==None):
            return 0
        if(root.left==None):
            return 1
        current=root
        self.depth=0
        while True:
            if current==None:
                break
            self.depth+=1
            current=current.left
        self.count=0
        
    def BFS(self,node,depth):
        if depth==self.depth-1:
            if node.left==None:
                return
            elif node.right==None:
                self.count+=1
                return
            else
                self.count+=2
                self.BFS(node.left,depth+1)
                self.BFS(node.right,depth+1)
        
        
