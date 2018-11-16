class Solution(object):
    def addBinary(self,a,b):
        inta=int(a,2)
        intb=int(b,2)
        s=inta+intb
        return bin(s)[2:]

if __name__=="__main__":
    s=Solution()
    print s.addBinary("10","1")
