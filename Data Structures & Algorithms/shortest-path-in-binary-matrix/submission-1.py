class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        def bfs(grid):
            

            visit = set()
            ROWS, COLS = len(grid) , len(grid[0])
            queue = deque()
            queue.append((0,0))
            visit.add((0,0))
            level = 1

            if grid[0][0] == 1:
                return -1


            while queue:
                for i in range(len(queue)):
                    r, c = queue.popleft()

                    if r == ROWS - 1 and c == COLS -1:
                        return level

                    diretions = [[0,1],[0,-1],[1,0],[-1,0], [1,1], [-1,-1], [1,-1], [-1,1]]
                    for dc, dr in diretions:
                        if r + dr == ROWS or c + dc == COLS or ( r + dr , c + dc) in visit or grid[r + dr][c + dc] == 1 or dc < 0 or dr < 0:
                            continue
                        queue.append((r + dr,c + dc))
                        visit.add((r + dr,c + dc))
                level += 1
            return - 1
                
        bfs(grid)

        return bfs(grid)


