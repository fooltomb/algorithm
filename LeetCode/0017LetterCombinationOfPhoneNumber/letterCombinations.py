class Solution:
    def letterCombinations(self, digits: str) :
        if digits=="":
            return []
        d={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        res=[""]
        for i in range(len(digits)):
            temp=[]
            for j in res:
                for k in d[digits[i]]:
                    temp.append(j+k)
            res=temp
        return res

if __name__=="__main__":
    s=Solution()
    r=s.letterCombinations("23")
    print(r)
    
            
        
