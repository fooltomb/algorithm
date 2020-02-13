class Sulotion(object):
    def lengthOfLongestSubstring(self,s):
        if s=='':
            return 0
        res=0
        cur=0
        for i in range(len(s)):
            for k in range(cur,i):
                if s[k]==s[i]:
                    cur=k+1;
            res=max(res,i-cur)
        return res+1
