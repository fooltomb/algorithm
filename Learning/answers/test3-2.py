class Solution:
    molar=''
    def MolarMass(self,str):
        self.molar=str
        sum=0
        temp=0
        for i in range(len(str)):
            if(str[i]=='C'):
                temp=12.01
                sum+=temp
            elif(str[i]=='H'):
                temp=1.008
                sum+=temp
            elif(str[i]=='O'):
                temp=16.00
                sum+=temp
            elif(str[i]=='N'):
                temp=14.01
                sum+=temp
            else:
                sum+=temp*(self.GetCount("",i)-1)
        print(sum)
    def GetCount(self,amount,index):
        try:
            count=int(self.molar[index])
            return self.GetCount(amount+self.molar[index],index+1)
        except:
            return int(amount)

if __name__=="__main__":
    so=Solution()
    #print(int('111'))
    while(True):
        s=input()
        if(s=="Exit"):
            break
        so.MolarMass(s)
            
