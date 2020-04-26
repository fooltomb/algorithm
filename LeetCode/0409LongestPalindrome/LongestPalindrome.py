class Solution:
    def longestPalindrome(self, s: str) -> int:
        self.dict={}
        for letter in s:
            if letter in self.dict:
                self.dict[letter]+=1
            else:
                self.dict[letter]=1
        one=0
        sum=0
        for value in self.dict.values():
            if(value%2==0):
                sum+=value
            else:
                sum+=value-1
                one=1
        return sum+one
        
