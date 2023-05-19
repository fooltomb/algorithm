class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        poisonedTime=0
        lastAttack=-duration
        for a in timeSeries:
            poisonedTime=poisonedTime+duration
            if a-lastAttack<duration:
                poisonedTime=poisonedTime-duration+a-lastAttack
            lastAttack=a
            
        return poisonedTime


if __name__=="__main__":
    so=Solution()
    print(so.findPoisonedDuration([1,2],2))
