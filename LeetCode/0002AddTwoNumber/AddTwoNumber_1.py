#Definiton for singly-linked list
class ListNode(object):
    def __init__(self,x):
        self.val=x
        self.next=None
class Solution(object):
    def addTwoNumbers(self,l1,l2):
        """
        """
        jinwei=0
        res=ListNode(0)
        brv=res
        while True:
            sum=l1.val+l2.val
            jinwei,res.val=sum//10,sum%10+jinwei
            if(res.val==10):
                res.val=0
                jinwei=1
            print res.val
            if(l1.next==None):
                l1.val=0
            else:
                l1=l1.next
            if(l2.next==None):
                l2.val=0
            else:
                l2=l2.next
            if(jinwei==0 and l1.next==None and l1.val==0 and l2.val==0 and l2.next==None):
                res=None
                break
            res.next=ListNode(0)
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
    res=s.addTwoNumbers(l1,l2)
    print res.val
    print res.next.val
    print res.next.next.val
    print res.next.next.next.val
    #print res.next.next.next.next.val




 
 
 

 
 
 
 
