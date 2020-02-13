class MyQueue(object):
    def __init__(self):
        self.q=[]
    def push(self,x):
        self.q.append(x)
    def pop(self):
        a=self.q[0]
        self.q.remove(a)
        return a
    def peek(self):
        return self.q[0]
    def empty(self):
        return len(self.q)==0
   
