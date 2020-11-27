class Solution:
    def findRadius(self, houses, heaters) -> int:
        res=0
        #radius=0
        houseIndex=0
        heaterIndex=0
        houseLength=len(houses)
        heaterLength=len(heaters)
        for i in range(houseLength):
            radius=abs(houses[i]-heaters[heaterIndex])
            for k in range(heaterIndex,heaterLength):
                if radius>=abs(houses[i]-heaters[k]):
                    radius=abs(houses[i]-heaters[k])
                else:
                    heaterIndex=k-1
                    break
            res=max(res,radius)
        return res
                


