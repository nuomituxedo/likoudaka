// Claire using DP using O(m*n) extra space
Runtime: 0 ms, faster than 100.00% of Java online submissions for Unique Paths.
Memory Usage: 33 MB, less than 5.02% of Java online submissions for Unique Paths.
​
class Solution {
public int uniquePaths(int m, int n) {
int[][] dp = new int[m][n]; // keep track of how many routes will pass by each cell
// initialize
for (int i = 0; i < m; i++)
dp[i][0] = 1;
for (int i = 0; i < n; i++)
dp[0][i] = 1;
//fill in dp matrix
for (int i = 1; i < m; i++){
for (int j = 1; j < n; j++){
dp[i][j] = dp[i-1][j] + dp[i][j-1];
}
}
return dp[m-1][n-1];
}
}
​
//Claire using DFS + backtracking
//Time Limit Exceeded on large input
class Solution {
int count;
public int uniquePaths(int m, int n) {
count = 0;
findpath(m,n,1,1);
return count;
}
public void findpath(int c, int r, int startc, int startr){
int i = startc, j = startr;
if (i == c && j == r)
count++;
if (i < c){
findpath(c, r, i+1, j);
}
if (j < r){
findpath(c, r, i, j+1);
}
}
}
​