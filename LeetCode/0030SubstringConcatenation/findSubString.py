class Solution:
    def findSubstring(self, s: str, words):
        lenWords=len(words)
        lenWord=len(words[0])
        lenSub=lenWords*lenWord
        res=[]
        for i in range(0,len(s)-lenSub+1):
            #print("i:"+str(i))
            copy=words.copy()
            flag=True
            for j in range(i,i+lenSub,lenWord):
                #print("j:"+str(j))
                temp=s[j:j+lenWord]
                try:
                    copy.remove(temp)
                except ValueError:
                    flag=False
                    break
            if flag:
                res.append(i)
        return res

if __name__=="__main__":
    s=Solution()
    r=s.findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake",["e"])
    print(r)
    #a=[2,3,4]
    #b=a.index(5)
    #print(b)
