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
        res=None
        brv=res
        while(sum/f!=0):
            if res==None:
                res=ListNode(sum//f)/(f/10)
            else:
                res.next=ListNode(sum//f)/(f/10)
            f*=10
            res=res.next
            




