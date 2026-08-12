class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # pick the fewest coins we want to pick the biggest coin and subtract it from the amount. issue is that we can go negative here so let me think idea is that we start at biggest then decrement acount the go through the list. basically pick right then go left if it is nrgative nevermind this does not work bc greedy does not pick the same coin twice
        
        #trying bottom up dp bc greedy was a mistake very sad :()

        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i-coin])

        if dp[amount] == float("inf"):
            return -1
        else:
            return dp[amount]  
