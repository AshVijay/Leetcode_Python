"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
] 
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""



class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        start = (0,0)
        end = (len(grid)-1, len(grid[len(grid)-1])-1)
        
        #Initialize a two-d-array
        twod_list = []
        new = []
        for i in range (end[0]+1):
          for j in range (end[1]+1):
             new.append(-1)
          twod_list.append(new)
          new = []
        
        
        #Dynamic programming based on tabulation
        for i in reversed(range(end[0]+1)):
          for j in reversed(range(end[1]+1)):
             if(i==end[0] and j==end[1]):
               twod_list[i][j] = grid[i][j]
               continue
             elif (i==end[0]):
               twod_list[i][j] = grid[i][j] + twod_list[i][j+1]
               continue 
             elif (j== end[1]):
               twod_list[i][j] = grid[i][j] + twod_list[i+1][j]
               continue
             twod_list[i][j] = grid[i][j] + min(twod_list[i+1][j],twod_list[i][j+1])
        
                 
        return (twod_list[0][0])
