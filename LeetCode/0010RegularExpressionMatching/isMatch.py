class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pattern=[]
        index=0
        while True:
            temp=p[index]
            if index+1<len(p) and p[index+1]=='*':
                temp+='*'
                index+=2
            else:
                index+=1
            pattern.append(temp)
            if index>=len(p):
                break
        return self.recurrent(s,pattern)
    def recurrent(self,s:str,pattern)->bool:
        #print(pattern)
        if s=="":
            if pattern==[]:
                return True
            for pat in pattern:
                if len(pat)==1:
                    return False
            return True
        else:
            if pattern==[]:
                return False
            if len(pattern[0])==1:
                if pattern[0]=='.' or pattern[0]==s[0]:
                    return self.recurrent(s[1:],pattern[1:])
                else:
                    return False
            else:
                if pattern[0][0]=='.':
                    for i in range(len(s)+1):
                        if self.recurrent(s[i:],pattern[1:]):
                            return True
                    return False
                else:
                    if self.recurrent(s,pattern[1:]):
                        return True
                    j=0
                    while(s[j]==pattern[0][0]):
                        if self.recurrent(s[j+1:],pattern[1:]):
                            return True
                        j+=1
                        if j>=len(s):
                            break
                    return False

                
if __name__=="__main__":
    s=Solution()
    #t=[1,2]
    #print(t[2:])
    print(s.isMatch("abbaaaabaabbcba","a*.*ba.*c*...."))
    print(s.isMatch("aa","a*"))
    print(s.isMatch("abbaaaabaabbcba",".*"))
    print(s.isMatch("acaabbaccbbacaabbbb","a*.*b*.*a*aa*a*"))
                
