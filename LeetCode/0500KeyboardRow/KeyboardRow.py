class Solution:
    def findWords(self,words):
        rows=["qwertyuiop","asdfghjkl","zxcvbnm"]
        res=[]
        for word in words:
            #yes=False
            for row in rows:
                here=False
                for letter in word.lower():
                    here=True
                    if row.find(letter)==-1:
                        here=False
                        break
                if here:
                    res.append(word)
                    break
        return res
