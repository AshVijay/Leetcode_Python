"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?
"""

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int: 
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if m == 1 and n == 1:
            if obstacleGrid[0][0] == 0 :
              return 1
            else:
              return 0
        dp = [[ 0 for i in range(n)] for i in range(m)]
        dp[0][0] = 1
        for i in range(m):
             for j in range(n):
                    if obstacleGrid[i][j] == 0 :
                        if j >0 and i>0 :
                          dp[i][j] =  ( dp[i][j-1] if obstacleGrid[i][j-1] == 0 else 0)  + (dp[i-1][j] if obstacleGrid[i-1][j] == 0 else 0)
                        if i == 0 and j >0:
                           dp[i][j] = dp[i][j-1] if obstacleGrid[i][j-1] == 0 else 0  
                        if j == 0 and i >0:
                           dp[i][j] =  dp[i-1][j] if obstacleGrid[i-1][j] == 0 else 0
                        if i==0 and j==0:
                             continue
        return dp[m-1][n-1]