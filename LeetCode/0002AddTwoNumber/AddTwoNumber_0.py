#Definition of singly-linked list
class ListNode(object):
    def __init__(self,x):
        self.val=x
        self.next=None
class Solution(object):
    def addTwoNumber(self,l1,l2):
        """
        """
        n1=0
        n2=0
        ln1=l1
        ln2=l2
        f=1

        while(ln1!=None):
            n1+=ln1.val*f
            f*=10
            ln1=ln1.next
        f=1
        while(ln2!=None):
            n2+=ln2.val*f
            f*=10
            ln2=ln2.next
        sum=n1+n2
        f=10
        res=ListNode(sum%f)
        sum=sum//f
        brv=res
        while(sum//f!=0 or sum%f!=0):
            res.next=ListNode(sum%f)
            sum=sum//f
            res=res.next
        return brv

if __name__=="__main__":
    
    l1=ListNode(2)
    l1.next=ListNode(4)
    l1.next.next=ListNode(3)
    l1.next.next.next=ListNode(6)
    l2=ListNode(5)
    l2.next=ListNode(6)
    l2.next.next=ListNode(4)
    s=Solution()
    res=s.addTwoNumber(l1,l2)
    print res.val
    print res.next.val
    print res.next.next.val
    print res.next.next.next.val
    print res.netx.next.next.next.val






