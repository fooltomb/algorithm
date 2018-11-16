class Solution(object):
    def plusOne(self,dits):
        index=len(dits)-1
        while True:
            if dits[index]!=9:
                dits[index]+=1
                return dits
            else:
                dits[index]=0
                index-=1
                if index==-1:
                    dits.insert(0,1)
                    return dits

if __name__=="__main__":
    s=Solution()
    print s.plusOne([9,9,9,9])


