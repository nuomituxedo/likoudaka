if visited[x][y]: continue
visited[x][y] = True
image[x][y] = color
self._fourDirections(x, y, queue, image, m, n)
return image
def _fourDirections(self, x, y, queue, image, m, n):
#left
if x > 0:
queue.append(image[x-1][y])
#right
if x < m-1:
queue.append(image[x+1][y])
#top
if y > 0:
queue.append(image[x][y+1])
#bottom
if y < n-1:
queue.append(image[x][y-1])
​
​
​
​
​
//BFS   Claire 11/2/2019
class Solution {
public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
int oldColor = image[sr][sc];
if (oldColor == newColor) return image;
Queue<int[]> q = new LinkedList<>();
int[][] directions = new int[][]{{0,1},{1,0},{0,-1},{-1,0}};
q.offer(new int[]{sr, sc});
while (!q.isEmpty()){
int[]cur = q.poll();
image[cur[0]][cur[1]] = newColor;
for (int[] dir : directions){
int x = cur[0] + dir[0];
int y = cur[1] + dir[1];
if (x < 0 || x >= image.length || y < 0 || y >= image[0].length || image[x][y] != oldColor) continue;