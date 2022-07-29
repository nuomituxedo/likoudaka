**Most voted solution:**
​
public int sumNumbers(TreeNode root) {
return sum(root, 0);
}
​
public int sum(TreeNode n, int s){
if (n == null) return 0;
if (n.right == null && n.left == null) return s*10 + n.val;
return sum(n.left, s*10 + n.val) + sum(n.right, s*10 + n.val);
}
--------
​
**Claire's own recursion beat 100% and 100%**
class Solution {
int sum = 0;
public int sumNumbers(TreeNode root) {
if (root == null) return 0;
pathSum(root, 0);
return sum;
}
public void pathSum(TreeNode node, int cursum){
cursum += node.val;
if (node.left == null && node.right == null) {
sum += cursum;
return;
}
if (node.left != null) pathSum(node.left, cursum*10);
if (node.right != null) pathSum(node.right, cursum*10);
return; // optional
}
}