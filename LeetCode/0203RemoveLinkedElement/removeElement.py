class Solution(object):
    def removeElements(self,head,val):
        if head==None:
            return None
        pre=head
        cur=head.next
        while(cur!=None):
            if cur.val==val:
                cur=cur.next
                pre.next=cur
            else:
                cur=cur.next
                pre=pre.next
        while head!=None and head.val==val
            head=head.next
        return head

