#输入正整数a,b,c,输出a/b的小数形式，精确小数点后c位
class Solution:
    def decimal(self,a,b,c):
        res=a*10**(c+1)//b
        res+=5
        res//=10
        res=res/10**c*1.0
        print(res)
if __name__ == "__main__":
    s=Solution()
    s.decimal(1,6,5)
    s.decimal(2,3,8)
