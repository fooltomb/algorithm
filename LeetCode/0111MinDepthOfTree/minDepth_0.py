class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution(object):
    def minDepth(self,root):
        listOfNode=[root]
        depth=0
        while listOfNode!=[]:
            depth+=1
            for i in len(listOfNode):
                if listOfNode[0]==None:
                    listOfNode=listOfNode[1:]
                    continue
                if listOfNode[0].left==None and listOfNode[0].right==None:
                    return depth
                listOfNode.append(listOfNode[0].left)
                listOfNode.append(listOfNode[0].right)
                listOfNode=listOfNode[1:]
