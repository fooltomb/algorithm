#abc:def:ghi 1:2:3
class Solution:
    def permutation(self):
        for i in range(123,330):
            a=str(i)
            b=str(i*2)
            c=str(i*3)
            res=a+b+c
            res=set(res)&set('123456789')
            if 9==len(res):
                print(a,b,c)
if __name__ == "__main__":
    s=Solution()
    s.permutation()