class Solution(object):
    def reverseVowels(self,s):
        l=list(s)
        vowels=['a','e','i','o','u']
        index=[]
        replace=[]
        for i in range(len(l)):
            if s[i].lower() in vowels:
                index.append(i)
                replace.append(s[i])
        replace.reverse()
        a=0
        for id in index:
            l[id]=replace[a]
            a+=1
        return ''.join(l)
