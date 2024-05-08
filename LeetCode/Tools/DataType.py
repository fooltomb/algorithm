#coding:utf-8
#定义单链表节点
class ListNode(object):
    def __init__(self,x):
        self.val=x
        self.next=None
#定义二叉树节点
class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
#字符串转换为树etc:"[2,2,3]"
def stringToTreeNode(input):
    input=input.strip()
    input=input[1:-1]
    if not input:
        return None

    inputValues=[s.strip() for s in input.split(',')]
    root=TreeNode(int(inputValues[0]))
    nodeQueue=[root]
    front=0
    index=1
    while index<len(inputValues):
        node=nodeQueue[front]
        front = front+1
        item=inputValues[index]
        index=index+1
        if item!='null':
            leftNumber=int(item)
            node.left=TreeNode(leftNumber)
            nodeQueue.append(node.left)
        if index>=len(inputValues):
            break
        item=inputValues[index]
        index+=1
        if item!='null':
            rightNumber=int(item)
            node.right=TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

def stringToListNode(input):
    input=input.strip()
    input=input[1:-1]
    if not input:
        return None
    inputValues=[s.strip() for s in input.split(',')]
    root=ListNode(int(inputValues[0]))
    cur=root
    for i in range(1,len(inputValues)):
        cur.next=ListNode(int(inputValues[i]))
        cur=cur.next
    return root

def listNodeToIntList(node):
    res=[]
    while node!=None:
        res.append(node.val)
        node=node.next
    return res
