from Tools.DataType import *

class Solution(object):
    def getIntersectionNode(self,headA,headB):
        if headA==None or headB==None:
            return None
        curA=headA
        curB=headB
        while curA!=None or curB!=None:
            if curA==curB:
                return curA
            curA=headB if curA==None else curA.next
            curB=headA if curB==None else curB.next
        return None
if __name__=="__main__":
    a=ListNode(1)
    a.next=ListNode(1)
    b=ListNode(2)
    c=ListNode(3)
    b.next=c
    a.next.next=c
    s=Solution()
    print s.getIntersectionNode(a,b)
