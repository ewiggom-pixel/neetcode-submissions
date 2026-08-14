class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        rows, cols = len(board), len (board[0])
        
        def dfs(r,c,board):

            if min(r,c) < 0 or r == rows or c == cols or board[r][c] != "O":
                return
            
            board[r][c] = "safe"
            dfs(r+1,c,board)
            dfs(r-1,c,board)
            dfs(r,c+1,board)
            dfs(r,c-1,board)

        
        for i in range(rows):
            dfs(i,0,board)
            dfs(i,cols-1,board)
        for j in range(cols):
            dfs(0,j,board)
            dfs(rows-1,j,board)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] ="X"
                if board[i][j] == "safe":
                    board[i][j] ="O"
