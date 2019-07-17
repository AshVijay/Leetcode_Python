"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
 
Output: 4
"""

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix == []:
             return 0
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0 for j in range(m)]  for i in range(n) ]
        dp[n-1][m-1] = int(matrix[n-1][m-1])
        i = n-2
    
        while i >=0 :
              j = m-2
              while j>=0 :
                if matrix[i][j] == "1":   
                   if matrix[i+1][j] == matrix[i][j+1] == matrix[i+1][j+1] == "1":
                                     
                                     dp[i][j] = 1+min(dp[i+1][j],dp[i][j+1],dp[i+1][j+1])
                   else:
                                     dp[i][j] = 1
                    
                j-=1
              i-=1
        maxSquare = 0
        for i in range(n):
             for j in range(m):       
                      if dp[i][j] >= maxSquare:
                              maxSquare = dp[i][j]
        return maxSquare*maxSquare
        