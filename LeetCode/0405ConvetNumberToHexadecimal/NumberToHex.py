class Solution:
    def toHex(self, num: int) -> str:
        self.hexdict={0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
        if(num==0):return '0'
        self.res=''
        if(num>0):
            self.getHex(num)
        else:
            self.getHex(4294967296+num)
        return self.res

    def getHex(self,num:int):
        self.res=self.hexdict[num%16]+self.res
        n=num//16
        if(n!=0):
            self.getHex(n)
