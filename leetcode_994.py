class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])

        fresh = set()
        rotten = set()

        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    fresh.add((i,j))
                elif grid[i][j]==2:
                    rotten.add((i,j))

        minutes=0
        while (len(fresh)>0):
            infected  = set()
            for rot in rotten.copy():
                i,j =rot
                if ((i+1),j) in fresh:
                    fresh.remove((i+1,j))
                    infected.add((i+1,j))
                if ((i,j+1)) in fresh:
                    fresh.remove((i,j+1))
                    infected.add((i,j+1))
                if ((i-1,j)) in fresh:
                    fresh.remove((i-1,j))
                    infected.add((i-1,j))
                if ((i,j-1)) in fresh:
                    fresh.remove((i,j-1))
                    infected.add((i,j-1))

            if len(infected)==0:
                return -1

            rotten = infected
            minutes+=1

        return minutes
