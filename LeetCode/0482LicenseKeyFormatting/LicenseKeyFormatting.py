class Solution:
    def licenseKeyFormatting(self, S, K):
        length=len(S)
        L=S.split('-')
        length=length+1-len(L)
        res="".join(L)
        
        value=res[0:length%K]
        for i in range(length%K,length,K):
            value=value+"-"+res[i:i+K]
        return value.upper() if length%K!=0 else value.upper()[1:]

if __name__=="__main__":
    s=Solution()
    res=s.licenseKeyFormatting("f-687jfhj-6",3)
    print(res)
