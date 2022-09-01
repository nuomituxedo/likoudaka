​
class Solution:
def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
ans, n, m = 0, len(grid), len(grid[0])
def trav(i: int, j: int) -> int:
if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] == 0: return 0
grid[i][j] = 0
return 1 + trav(i-1, j) + trav(i, j-1) + trav(i+1, j) + trav(i, j+1)
for i, j in product(range(n), range(m)):
if grid[i][j]: ans = max(ans, trav(i, j))
return ans
​
//Claire's DFS no extra memory
Runtime: 2 ms, faster than 100.00%  Memory Usage: 43.8 MB, less than 50.00%
class Solution {
public int maxAreaOfIsland(int[][] grid) {
if (grid.length == 0) return 0;
int m = grid.length;
int n = grid[0].length;
int max = 0;
for (int i = 0; i < m; i++){
for (int j = 0; j < n; j++){
if (grid[i][j] == 1)
max = Math.max(max, findmax(grid, i, j));
}
}
return max;
}
private int findmax(int[][] grid, int i, int j){
int m = grid.length;
int n = grid[0].length;
int area = 0;
if (i<0 || i>=m || j<0 || j>=n || grid[i][j] == 0)
return 0;
grid[i][j] = 0;
area =  1 + findmax(grid, i+1, j) + findmax(grid,i-1,j) + findmax(grid, i, j+1) + findmax(grid, i, j-1);
return area;
}
}