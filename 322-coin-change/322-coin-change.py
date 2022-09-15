class Solution:
    #DP Top-Down
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        print(dp)
        for coin in coins:
            for i in range(coin, amount+1):
                if dp[i-coin] != float('inf'):
                    dp[i] = min(dp[i-coin]+1, dp[i])
        return -1 if dp[amount]==float('inf') else dp[amount]