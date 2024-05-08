from Tools.DataType import *
#import pascalTriangle_0 as SO
#from 0222CountCompleteTreeNode.CountCompleteTreeNode import Solution
#import 0024SwapNodesInPairs.swapPairs.Solution

if __name__=="__main__":
    #root=stringToTreeNode("[5,4,8,11,12,13,4,7,2,15,22,7,1]")
    #print(root.right.left.right.val)
    head=stringToListNode("[1,2,3,4,5]")
    res=ListNode(1)
    cur=res
    while True:
        if head!=None and head.next!=None:
            res.next=ListNode(head.next.val)
            res=res.next
            res.next=ListNode(head.val)
            res=res.next
            head=head.next.next
        elif head!=None:
            res.next=ListNode(head.val)            
            break
        else:
            break
    res=listNodeToIntList(cur.next)
    print(res)


