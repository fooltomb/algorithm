#Definition for singly-linked list
class ListNode(object):
    def __init__(self,x):
        self.val=x
        self.next=None
class Solution(object):
    def mergeTwoLists(self,l1,l2):
        res=ListNode(0)
        brv=res
        while True:
            if l1==None and l2==None:
                break
            elif l1==None:
                res.next=l2
                break
            elif l2==None:
                res.next=l1
                break
            elif l1.val>=l2.val:
                res.next=ListNode(l2.val)
                l2=l2.next
            else:
                res.next=ListNode(l1.val)
                l1=l1.next
            res=res.next
        return brv.next
if __name__=="__main__":
    a=ListNode(8)
    a.next=ListNode(12)
    b=ListNode(5)
    b.next=ListNode(6)
    b.next.next=ListNode(9)
    s=Solution()
    res=s.mergeTwoLists(a,b)
    print res.val
    print res.next.val
    print res.next.next.val
    print res.next.next.next.val
    print res.next.next.next.next.val
