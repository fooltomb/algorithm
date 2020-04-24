class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        for letter in ransomNote:
            index=magazine.find(letter)
            if index==-1:
                return False
            else:
                magazine=magazine[:index]+magazine[index+1:]
        return True

if __name__=="__main__":
    s=Solution()
    print(s.canConstruct("aa","ab"))
        
