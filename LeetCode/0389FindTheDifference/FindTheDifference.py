class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for letter in t:
            index=s.find(letter)
            if index==-1:
                return letter
            else:
                s=s[:index]+s[index+1:]
