#这个答案是错误的，因为要判断给的数字是不是int32
class Solution(object):
    def reverse(self,x):
        """
        """
        res=""
        if(x>0):
            s=str(x)
        else:
            s=str(-x)
        for i in range(len(s)):
            res+=s[-i-1]
        if(x>0):
            return int(res)
        else:
            return -int(res)

if __name__=="__main__":
    s=Solution()
    print s.reverse(-989090)

