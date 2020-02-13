class NumArray(object):
    def __init__(self,nums):
        self.n=nums
    def sumRange(self,i,j):
        return sum(self.n[i:j+1])

