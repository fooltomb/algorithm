class Solution:
    def findDaffdil(self):
        for i in range(100,1000):
            a=i%10
            b=(i%100)//10
            c=i//100
            if i==a*a*a+b*b*b+c*c*c:
                print(i)

if __name__=="__main__":
    s=Solution()
    s.findDaffdil()
