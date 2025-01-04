"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
 
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""

#1) 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapper = {}
        final = []
        for i in range(len(nums)):
              if nums[i] not in mapper.keys():
                      mapper[target-nums[i]] = i
              else:
                   final = [mapper[nums[i]],i]
        return final

#2)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffMap = {} # map from diff value to index of element being subtracted
        for i in range(len(nums)):
            if nums[i] in diffMap: 
                return [diffMap[nums[i]], i]
            diffMap[target - nums[i]] = i