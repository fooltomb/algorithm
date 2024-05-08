class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists):
        res=None
        cur=None
        while True:
            minVal=0
            flag=False
            index=0
            done=0
            for i in range(len(lists)):
                if lists[i]==None:
                    done+=1
                    continue
                else:
                    if flag==False:
                        minVal=lists[i].val
                        index=i
                        flag=True
                    else:
                        if lists[i].val<minVal:
                            minVal=lists[i].val
                            index=i
                        
            if done==len(lists):
                break
            if res==None:
                res=ListNode(lists[index].val,None)
                cur=res
            else:
                cur.next=ListNode(lists[index].val,None)
                cur=cur.next
            lists[index]=lists[index].next
        return res
            
