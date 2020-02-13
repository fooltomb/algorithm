class Solution(object):
    def isPowerOfThree(self,n):
        if n=0:return False
        if n==3 or n==1:return True
        if n%3!=0:return False
        else:return self.isPowerOfThree(n/3)
#还有个办法：就是转换成3进制，这样1000...000这个格式就3的n次方
