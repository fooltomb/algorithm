class Solution:
    def islandPerimeter(self,grid):
        if not grid:return 0
        n, m =len(grid), len(grid[0])
        def check(x, y):
            if 0<=x<n and 0<=y<m:
                return grid[x][y]
            return 0
        dirc = [(1,0), (0,1), (-1, 0), (0,-1)]
        area = 0
        for i in range(0, n):
            for j in range(0, m):
                if grid[i][j]==1:
                    area+=4
                    for k, v in dirc:
                        area-=check(i+k, j+v)
        return area

        


