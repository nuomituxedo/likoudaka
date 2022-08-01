//From discussion: using DFS + PQ
​
class Solution {
public List<List<Integer>> verticalTraversal(TreeNode root) {
List<List<Integer>> res = new ArrayList();
if (root == null) return res;
PriorityQueue<Point> pq = new PriorityQueue(new Comparator<Point>(){
public int compare(Point p1, Point p2){
if (p1.x != p2.x)
return p1.x - p2.x;
else if (p1.y != p2.y)
return p2.y - p1.y;
else
return p1.val - p2.val;
}
});
dfs(root, 0, 0, pq);
int prev_x = Integer.MIN_VALUE;
while (!pq.isEmpty()){
Point p = pq.poll();
if (p.x > prev_x){
List<Integer> list = new ArrayList();
list.add(p.val);
res.add(list);