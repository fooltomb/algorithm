class Solution:
    def numberOfBoomerangs(self, points) -> int:
        res=0
        for i in range(len(points)):
            disDict={}
            for j in range(len(points)):
                if i==j:
                    continue
                distance=self.getDistance(points[i],points[j])
                if distance in disDict:
                    disDict[distance]+=1
                else:
                    disDict[distance]=1
            for value in disDict.values():
                for k in range(value):
                    res+=k
        return res
            

    def getDistance(self,point1,point2)->int:
        return (point1[0]-point2[0])**2+(point1[1]-point2[1])**2
