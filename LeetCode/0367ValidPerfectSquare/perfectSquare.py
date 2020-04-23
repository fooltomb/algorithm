class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num==1:
            return True
        a=1
        while(num>a*a):
            a-=1
            if(a*a==num):
                return True
        return False
