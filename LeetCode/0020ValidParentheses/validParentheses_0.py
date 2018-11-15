class Solution(object):
    def isValid(self,s):
        """
        """
        dict={'(':'-',')':'(','[':'-',']':'[','{':'-','}':'{'}
        if len(s)==0:
            return True
        stack=[s[0]]
        for i in range(1,len(s)):
            if len(stack)==0 or dict[s[i]]!=stack[-1]:
                stack.append(s[i])
            else:
                stack.pop()
        return True if len(stack)==0 else False

if __name__=="__main__":
    s=Solution()
    print s.isValid("(){}(())[)]")








