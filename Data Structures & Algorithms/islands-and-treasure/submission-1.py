class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        


        rows, cols = len(grid), len(grid[0])
        queue = deque()
        visit = set()
        INF = 2147483647

        def bfs(r, c):      
            if c < 0 or r <0 or r == rows or c== cols or grid[r][c] == -1 or  (r, c ) in visit:
                return
            queue.append((r,c))
            visit.add((r,c))
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append([i,j])
                    visit.add((i,j))

        distance = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c]= distance
                
                bfs(r+1,c)
                bfs(r-1,c)
                bfs(r,c+1)
                bfs(r,c-1)
            distance += 1 



                
            


        


            

