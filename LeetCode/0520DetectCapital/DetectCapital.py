class Solution:
    def detectCapitalUse(self,word):
        frist=(word[0].upper()==word[0])
        if not frist:
            for i in range(1,len(word)):
                if word[i].upper()==word[i]:
                    return False
            return True
        else:
            print("first letter is upper")
            second=(word[1].upper()==word[1])
            if second:
                print("second letter is upper")
                for i in range(2,len(word)):
                    if word[i].upper()!=word[i]:
                        return False
                return True
            else:
                for i in range(2,len(word)):
                    if word[i].upper()==word[i]:
                        return False
                return True
        return True

if __name__=="__main__":
    s=Solution()
    print(s.detectCapitalUse("USA"))
