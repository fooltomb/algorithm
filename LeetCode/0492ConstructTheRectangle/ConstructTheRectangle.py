class Solution:
    def constructRectangle(self, area):
        #L=int(area**0.5)
        for i in range(1,(area//2)+1):
            if area%i==0 and i>=area//i:
                    return [i,area//i]
        return [area,1]


if __name__=="__main__":
    s=Solution()
    res=s.constructRectangle(14)
    print(res)
