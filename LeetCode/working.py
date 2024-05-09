from Tools.DataType import *
#import pascalTriangle_0 as SO
#from 0222CountCompleteTreeNode.CountCompleteTreeNode import Solution
#import 0024SwapNodesInPairs.swapPairs.Solution

class Solution:
    def reverseKGroup(self, head, k: int):
        h=ListNode(0)
        res=h
        while True:            
            cur=[]
            for i in range(k):
                cur.append(head)
                head=head.next
            for i in range(k):
                res.next=cur.pop()
                res=res.next
            if head==None:
                break
        return h.next
if __name__=="__main__":
    #root=stringToTreeNode("[5,4,8,11,12,13,4,7,2,15,22,7,1]")
    #print(root.right.left.right.val)
    head=stringToListNode("[1,2,3,4,5,6]")
    s=Solution()
    cur=s.reverseKGroup(head,2)
    res=listNodeToIntList(cur)
    print(res)


