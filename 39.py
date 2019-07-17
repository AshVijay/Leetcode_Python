"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7], 
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""

class Solution:
    final = [] 
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.final = []
        self.recurse(candidates, target, [])
        return self.final
        
    def recurse(self, candidates , target , tempList):
        if target < 0 :
              return 0
        elif target == 0 and sorted(tempList) not in self.final:
              self.final.append(sorted(tempList))   
        else:
              for i in range(len(candidates)):
                     tempList.append(candidates[i])
                     self.recurse(candidates, target- candidates[i], tempList)
                     tempList.remove(candidates[i])