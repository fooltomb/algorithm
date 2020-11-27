class Solution:
    def findComplement(self,num):
        length=len(bin(num))-2
        return (2**length-1)^num
if __name__=="__main__":
    s=Solution()
    res=s.findComplement(5)
    print(res)
