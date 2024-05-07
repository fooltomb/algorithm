class ListNode:
    def __init__(self, val=0, next=None):
       self.val = val
       self.next = next
class Solution:
    def removeNthFromEnd(self, head, n: int):
        current=head
        for i in range(n):
            current=current.next
        res=ListNode(-1,head)
        while current!=None:
            current=current.next
            res=res.next
        if(res.val==-1):
            return head.next
        res.next=res.next.next
        return head
    
