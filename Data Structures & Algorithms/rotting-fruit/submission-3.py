class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid) , len(grid[0])
        queue = deque()
        visit = set()
        fresh_count = 0

        def bfs(r,c):

            if min(r,c) < 0 or (r,c) in visit or r == rows or c == cols or grid[r][c] == 0:
                return
            queue.append([r,c])
            visit.add((r,c))
            if grid[r][c] == 1:
                grid[r][c] = 2
                nonlocal fresh_count
                fresh_count -= 1
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append([i,j])
                    visit.add((i,j))
                elif grid[i][j] == 1:
                    fresh_count += 1
        
        if fresh_count == 0: return 0
        distance = -1
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                bfs(r+1,c)
                bfs(r-1,c)
                bfs(r,c+1)
                bfs(r,c-1)
            distance += 1
        if not any(1 in stuff for stuff in grid):
            return distance  
        else:
            return -1

