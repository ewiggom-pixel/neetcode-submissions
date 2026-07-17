class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i, order in enumerate(matrix):
            
            L, R = 0, len(order) - 1

            while L <= R:
                Mid = (L+R)// 2
                if target > order[Mid]:
                    L = Mid + 1
                elif target < order[Mid]:
                    R = Mid - 1
                else: 
                    if target == order[Mid]:
                        return True
        return False

