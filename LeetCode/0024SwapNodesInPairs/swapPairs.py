class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head):
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
        return cur.next
