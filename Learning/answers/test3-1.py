class Solution:
    def Score(self,str):
        sum=0
        temp=0
        for i in range(len(str)):
            if(str[i]=='X'):
                temp=0
            elif(str[i]=='O'):
                temp+=1
                sum+=temp
        print(sum)

if __name__=="__main__":
    so=Solution()
    while(True):
        s=input()
        if(s=="Exit"):
            break
        so.Score(s)
            
