class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh, rotten = set(), set()
        if not grid or not grid[0]:return -1
        R, C = len(grid), len(grid[0])
        for i in range(R):
            for j in range(C):
                if grid[i][j]==1:
                    fresh.add((i,j))
                elif grid[i][j]==2:
                    rotten.add((i,j))
        if not fresh:return 0
        if not rotten:return -1
        
        res = 0
        while rotten:
            res += 1
            new_rotten = set()
            for i,j in rotten:
                for di, dj in [(-1, 0),(1, 0),(0, 1),(0, -1)]:
                    r, c = i+di, j+dj
                    if (r,c) in fresh:
                        new_rotten.add((r,c))
            if not new_rotten:return -1
            fresh -= new_rotten
            rotten = new_rotten
            if not fresh:return res