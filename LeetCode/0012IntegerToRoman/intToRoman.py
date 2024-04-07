class Solution:
    def intToRoman(self, num: int) -> str:
        res=""
        m=num//1000
        for i in range(m):
            res+='M'
        num=num%1000
        c=num//100
        res+=self.getRoman(c,'C','M','D')
        num=num%100
        x=num//10
        res+=self.getRoman(x,'X','C','L')
        num=num%10
        res+=self.getRoman(num,'I','X','V')
        return res

    def getRoman(self,count,one,full,half)->str:
        if count==1:
            return one
        if count==2:
            return one+one
        if count==3:
            return one+one+one
        if count==4:
            return one+half
        if count==5:
            return half
        if count==6:
            return half+one
        if count==7:
            return half+one+one
        if count==8:
            return half+one+one+one
        if count==9:
            return one+full
        return ""

if __name__=="__main__":
    s=Solution()
    print(s.intToRoman(3))
    print(s.intToRoman(58))
    print(s.intToRoman(1994))
