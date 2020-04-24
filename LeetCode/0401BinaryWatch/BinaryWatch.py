class Solution:
    def readBinaryWatch(self, num: int):
        self.res=[]
        self.lights=[0,0,0,0,0,0,0,0,0,0]
        self.num=num-1
        self.addLight(0)

            
        return self.res
    def addLight(self,index:int):
        for i in range(index,10):
            self.lights[i]=1
            if(self.num==0):
                self.getTime()
            else:
                self.num-=1
                self.addLight(i+1)
                self.num+=1
            self.lights[i]=0
            

    def getTime(self):
        hour=self.lights[0]*8+self.lights[1]*4+self.lights[2]*2+self.lights[3]
        minute=self.lights[4]*32+self.lights[5]*16+self.lights[6]*8+self.lights[7]*4+self.lights[8]*2+self.lights[9]
        if(minute>59 or hour>11):
            return
        if(minute<10):
            self.res.append(str(hour)+":0"+str(minute))
        else:
            self.res.append(str(hour)+":"+str(minute))

if __name__=="__main__":
    s=Solution()
    print (s.readBinaryWatch(3))
