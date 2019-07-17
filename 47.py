
"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1] 
]

"""


class Solution:
    final = []
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.final = []
        if len(nums) == 0 :
              return []
        self.backtrack( 0, nums, [[]])
        return self.final
    
    def backtrack(self, start, remList, tempList):
        if len(remList) == 0 and sorted(tempList)[0] not in self.final:
               self.final.append(sorted(tempList)[0])
        savedList = tempList        
        
        for i in range(len(remList)):
            temp = remList.pop(i)
            tempList = [ element+[temp]  for element in tempList]
            self.backtrack(i+1, remList, tempList)
            tempList = savedList
            remList.insert(i,temp)