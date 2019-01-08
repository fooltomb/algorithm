class Solution(object):
    def hammingWeight(self,n):
        bit=bin(n)
        count=0
        for i in range(len(bit)):
            if bit[i]=="1":
                count+=1
        return count
