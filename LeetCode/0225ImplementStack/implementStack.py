class MyStack(object):
    def __init__(self):
        self.s=[]
    def push(self,x):
        self.s.append(x)
    def pop(self):
        return self.s.pop()
    def top(self):
        return self.s[-1]
    def empty(self):
        return len(self.s)==0
