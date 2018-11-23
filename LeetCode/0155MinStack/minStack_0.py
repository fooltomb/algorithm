class MinStack(object):
    def __init__(self):
        self.min=[]
        self.stack=[]
    def push(self,x):
        if self.min==[]:
            self.min.append(x)
        else:
            self.min.append(min(x,self.min[-1]))
        self.stack.append(x)
    def pop(self):
        self.stack.pop()
        self.min.pop()
    def top(self):
        return self.stack[-1]
    def getMin(self):
        return self.min[-1]
    
