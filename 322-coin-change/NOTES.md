int min = Integer.MAX_VALUE;
for (int coin : coins) {
int res = coinChange(coins, rem - coin, count);
if (res >= 0 && res < min)
min = 1 + res;
}
count[rem - 1] = (min == Integer.MAX_VALUE) ? -1 : min;
return count[rem - 1];
}
}
=======================
//Claire redoing approach 3: DP Top-Down
class Solution {
public int coinChange(int[] coins, int amount) {
if (amount < 1) return 0;
return mincoins(coins, amount, new int[amount]);
}
private int mincoins(int[] coins, int remainder, int[] count){
if (remainder < 0) return -1; // the set of coins exceeded target amount
if (remainder == 0) return 0; // the set of coins equal target amount
if (count[remainder -1] != 0) //  remainder already has a solution, return it
return count[remainder-1];
int min = Integer.MAX_VALUE;
for (int coin : coins){
// try every coin to find the fewest coin combination
//recursion (top down: start with larger number)
// recurse with (amount - coin)
int res = mincoins(coins, remainder - coin, count);
if (res >= 0 && res < min)
min = 1 + res;
//or: if (res >= 0)  min = Math.min(min, 1 + res);
}
count[remainder - 1] = (min == Integer.MAX_VALUE)? -1 : min;
return count[remainder - 1];
}
}