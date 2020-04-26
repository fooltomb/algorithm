class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        minlen=min(len(num1),len(num2))
        temp=0
        res=''
        for i in range(1,minlen+1):
            s=int(num1[-i])+int(num2[-i])+temp
            res=str(s%10)+res
            temp=s//10
        if len(num2)>=len(num1):
            for i in range(minlen+1,len(num2)+1):
                s=int(num2[-i])+temp
                res=str(s%10)+res
                temp=s//10
        else:
            for i in range(minlen+1,len(num1)+1):
                s=int(num1[-i])+temp
                res=str(s%10)+res
                temp=s//10
        if temp==1:
            res="1"+res
        return res

if __name__=="__main__":
    s=Solution()
    print(s.addStrings("1065467645766476","9978678456"))
    print(1065467645766476+9978678456)
