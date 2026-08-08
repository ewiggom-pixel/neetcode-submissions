class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0
        visit = set()
        def dfs(grid,r,c,visit):

            if (min(r,c)< 0 or r == rows or c == cols or (r,c) in visit) or grid[r][c] == "0":
                return 

            visit.add((r,c))

            
            dfs(grid, r + 1, c, visit)
            dfs(grid, r - 1, c, visit)
            dfs(grid, r, c + 1, visit)
            dfs(grid, r, c - 1, visit)

            

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visit:
                    dfs(grid,i,j,visit)
                    count += 1
        return count