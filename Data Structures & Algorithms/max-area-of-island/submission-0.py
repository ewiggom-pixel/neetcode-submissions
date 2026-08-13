class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        visit = set()
        max_count = 0
        r, c = len(grid) , len(grid[0])
        def dfs(m,n):


            if m < 0 or n < 0 or m >= r or n >= c or grid[m][n] != 1 or (m,n) in visit:
                return 0 

            visit.add((m,n))
            count = 1 
            count += dfs(m+1,n)
            count += dfs(m-1,n)
            count += dfs(m,n+1)
            count += dfs(m,n-1)


            return count

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1 and (i,j) not in visit:
                    max_count = max(max_count, dfs(i,j))

        return max_count
