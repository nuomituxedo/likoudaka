​
//Claire DFS 8/23/19
class Solution {
public int maxDepth(TreeNode root) {
if (root == null) return 0;
return Math.max(maxDepth(root.left), maxDepth(root.right)) + 1;
}
}
====
//Claire BFS 8/23/19
class Solution {
public int maxDepth(TreeNode root) {
if (root == null) return 0;
Queue<TreeNode> q = new LinkedList<>();
q.offer(root);
int level = 0;
while (!q.isEmpty()){
int size = q.size();
for (int i = 1; i <= size; i++){
TreeNode cur = q.poll();
if (cur.left!= null) q.offer(cur.left);
if (cur.right!=null) q.offer(cur.right);
}
level++;
}
return level;