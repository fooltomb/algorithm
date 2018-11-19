class ListNode(object):
    def __init__(self,x):
        self.val=x
        self.next=None
class Solution(object):
    def deleteDuplictes(self,head):
        cur=head
        while(cur.next!=None):
            if cur.val==cur.next.val:
                cur.next=cur.next.next
            else:
                cur=cur.next
                if cur==None:
                    break
        return head

