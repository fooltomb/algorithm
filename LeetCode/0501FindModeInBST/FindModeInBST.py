class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution:
    def findMode(self,root):
        self.res=[]        
        self.inOrderRootRecursionDisplay(root)
        maxCount=0
        currentCount=0
        last=self.res[0]
        result=[]
        for num in self.res:
            if num==last:
                currentCount+=1
            else :
                if currentCount==maxCount:
                    result.append(last)
                elif currentCount>maxCount:
                    maxCount=currentCount
                    result=[last]
                last=num
                currentCount=1
        if currentCount==maxCount:
            result.append(last)
        elif currentCount>maxCount:
            maxCount=currentCount
            result=[last]
        return result
    def inOrderRootRecursionDisplay(self,node):
        if(node.left!=None):
            self.inOrderRootRecursionDisplay(node.left)
        self.res.append(node.val)
        if(node.right!=None):
            self.inOrderRootRecursionDisplay(node.right)
        
                
