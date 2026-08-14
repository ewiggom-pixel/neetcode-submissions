class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        result = [[]]

        pac = set()
        alt= set()
        rows, cols = len(heights), len(heights[0]) 


        def dfs(r,c,visit,prev_height):

            
            if min(r,c) < 0 or r == rows or c == cols or (r,c) in visit or heights[r][c] < prev_height:
                return

            visit.add((r,c))
            dfs(r+1,c,visit, heights[r][c])
            dfs(r-1,c,visit, heights[r][c])
            dfs(r,c-1,visit, heights[r][c])
            dfs(r,c+1,visit, heights[r][c])
 
        for i in range(cols):
            dfs(0,i,pac,heights[0][i])
            dfs(rows-1,i,alt,heights[rows-1][i])
        for j in range(rows):
            dfs(j,0,pac,heights[j][0])
            dfs(j,cols-1,alt,heights[j][cols-1])

        result = []
        for i in range(rows):
            for j in range(cols):
                if (i,j) in pac and (i,j) in alt:
                    result.append([i,j])

        return result 



