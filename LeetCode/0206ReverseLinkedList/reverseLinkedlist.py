class Solution(object):
    def reverseList(self,head):
        if head==None:
            return None
        temp=head
        prev=None
        while temp!=None:
            head=temp
            temp=temp.next
            head.next=prev
            prev=head
        return prev
