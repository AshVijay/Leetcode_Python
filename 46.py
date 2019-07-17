"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
] 

"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        return self.helper(nums)
        
        
        
    def helper(self, subset):
    
        if len(subset) == 1 :
            return [subset]
        temp = []
        for i in range(len(subset)):
            temp_list = self.helper( subset[:i]+subset[i+1:] )
            [ temp.append(i) for i in [ [subset[i]]+ele for ele in temp_list]]
        return temp
        
   