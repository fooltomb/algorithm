from Tools.DataType import *
class Solution(object):
    def hasCycle(self,head):
        fastNode=head
        slowNode=head
        while fastNode!=None and fastNode.next!=None:
            if fastNode.next==slowNode or fastNode.next.next==slowNode:
                return True
            fastNode=fastNode.next.next
            slowNode=slowNode.next
        
        return False

if __name__=="__main__":
    a=ListNode(2)
    b=ListNode(2)
    c=ListNode(2)
    a.next=b
    b.next=c
    c.next=b
    s=Solution()
    print s.hasCycle(a)
