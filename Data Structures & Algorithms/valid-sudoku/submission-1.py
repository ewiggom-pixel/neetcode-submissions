class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        c = defaultdict(set)
        r = defaultdict(set)
        part = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                box_key = (i // 3, j // 3)
                if board[i][j] in c[i] or board[i][j] in r[j] or board[i][j] in part[box_key]:
                    return False
                c[i].add(board[i][j])
                r[j].add(board[i][j])
                part[box_key].add(board[i][j])
        return True
