class Solution(object):
    def reverseBits(self,n):
        return int(bin(n)[:1:-1]+"0"*(32-len(bin(n))+2),2)
