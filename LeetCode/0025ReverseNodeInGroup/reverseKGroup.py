class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head, k: int):
        h=ListNode()
        res=h
        while True:            
            cur=[]
            for i in range(k):
                if head==None:
                    res.next=cur[0]
                    return h.next                
                cur.append(head)
                head=head.next
            for i in range(k):
                res.next=cur.pop()
                res=res.next
            res.next=None
            if head==None:
                break
        return h.next
