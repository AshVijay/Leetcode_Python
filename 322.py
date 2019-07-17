
"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2: 

Input: coins = [2], amount = 3
Output: -1
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf") for i in range(amount+1)]
        dp[0] = 0
        for i in range(1,amount+1) :
             self.helper(coins,i,dp)
        return dp[-1] if dp[-1] != float("inf") else -1
    
    def helper(self, coins, amount, dp):
            val = float("inf")
            for coin in coins:
               if coin <= amount:
                     val = dp[amount-coin]
                     if 1+ val < dp[amount] and val!= float("inf")  :
                                   dp[amount] = val+1

            