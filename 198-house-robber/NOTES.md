**Claire's DP solution beats 100% and 100%:**
​
class Solution {
public int rob(int[] nums) {
if (nums == null || nums.length == 0) return 0;
if (nums.length == 1) return nums[0];
int[] dp = new int[nums.length];
dp[0] = nums[0];
dp[1] = Math.max(nums[0], nums[1]);
for (int i = 2; i < nums.length; i++){
dp[i] = Math.max(dp[i-1], (dp[i-2] + nums[i]));
}
return dp[nums.length-1];
}
}
​
------
//DP from solution, much neater than Claire's DP
//and Space complexity = O(1). big improvement!
​
class Solution {
public int rob(int[] nums) {
int prevMax = 0;
int currMax = 0;
for (int x : nums) {
int temp = currMax;
currMax = Math.max(prevMax + x, currMax);
prevMax = temp;
}
return currMax;
}
}