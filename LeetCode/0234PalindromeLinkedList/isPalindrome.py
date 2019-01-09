class Solution(object):
    count=0
    cur=head
    while cur!=None:
        count+=1
        cur=cur.next
    if count<2:
        return True
    cur=head
    pre=None
    for index in range(0,count):
        if index<(count-1.1)/2:
            head=cur
            cur=cur.next
            head.next=pre
            pre=head
        elif index>(count-0.9)/2:
            if cur.val!=pre.val:
                return False
            cur=cur.next
            pre=pre.next
        else:
            cur=cur.next
    return True

