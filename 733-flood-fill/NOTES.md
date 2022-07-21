class Solution:
def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
m = len(image)
n = len(image[0])
visited = [[None for _ in range(n)] for _ in range(m)]
initialColor = image[sr][sc]
queue = [(sr,sc)]
while queue:
sr, sc = queue.pop(0)
print('current:', sr, sc)
print('queue', queue)
if image[sr][sc] == initialColor:
print('update color')
if visited[sr][sc]: continue
visited[sr][sc] = True
image[sr][sc] = newColor
self._fourDirections(sr, sc, queue, image, m, n)
return image
def _fourDirections(self, x, y, queue, image, m, n):
print('jojo', x, y, queue, image, m, n)
#left
if x > 0:
queue.append((x-1, y))
print('left', x-1, y)
#right
if x < m-1:
queue.append((x+1, y))
print('right', x+1, y)
#top
if y > 0:
queue.append((x, y-1))
print('top', x, y-1)
#bottom
if y < n-1:
queue.append((x, y+1))
print('bottom', x, y+1)
print('image',image)
​
​
​
​
​
​
//BFS   Claire 11/2/2019
class Solution {
public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
int oldColor = image[sr][sc];
//BFS   Claire 11/2/2019