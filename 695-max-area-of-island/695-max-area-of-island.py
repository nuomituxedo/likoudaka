class Solution:
    #DFS
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        m = len(grid)
        n = len(grid[0])
        
        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0:
                return 0
            
            grid[x][y] = 0 #mark visited
            
            return 1 + dfs(x-1,y) + dfs(x+1,y) + dfs(x,y-1) + dfs(x,y+1)
        
        for i, j in product(range(m), range(n)):
            if grid[i][j] == 1:
                maxArea = max(maxArea, dfs(i, j))
        return maxArea
                    
        
