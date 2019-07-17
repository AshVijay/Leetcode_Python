
"""
746. Min Cost Climbing Stairs
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
Note:
cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].
"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:     
        dp = [-1 for ele in range(len(cost)+1)]
        dp[0] = 0
        dp[1] = 0 
        self.helper(cost, dp , len(cost))
        print(dp)
        return dp[-1]
    
    def helper(self, cost, dp , k ):
        if k >= 2:
             if dp[k-1] == -1 or dp[k-2]==-1:
                    dp[k] = min(self.helper(cost,dp,k-1)+cost[k-1],self.helper(cost,dp,k-2)+cost[k-2])
             else:
                    dp[k] = min(dp[k-1]+cost[k-1],dp[k-2]+cost[k-2])
        return dp[k]
        