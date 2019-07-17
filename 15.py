"""

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is: 
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
             return []
        final = []
        for i in range(len(nums)-2): 
              target = -nums[i]
              mapper = {}
              for j in range(i+1,len(nums)):
                   if nums[j] not in mapper.keys():
                          mapper[target - nums[j]] = nums[j]
                   else: 
                      temp  = sorted([nums[i],mapper[nums[j]],nums[j]])
                      if temp not in final :
                       final.append(temp)
        return final