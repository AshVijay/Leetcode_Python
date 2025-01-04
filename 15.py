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

#1 (O(N^2)) (Time limit exceeded) 

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




#2 (O(N*log(N)) 


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        resultList = []
        nums = sorted(nums)
        length = len(nums)
        i = 0
        j = i+1
        k = length-1 
        # iterate till the last permissible value for 1
        while i < (length-2):
            curSum = nums[i] + nums[j] + nums[k]
            if curSum == 0:
                resultList.append([nums[i], nums[j], nums[k]]) 
                j+=1
                k-=1
                # iterate till last permissible value for "j" while ignoring duplicate candidates for 
                # the second position in the triplet
                while j < length-1 and nums[j] == nums[j-1]:
                    j+=1
                # iterate till last permissible value for "k" while ignoring duplicate candidates for 
                # the third position in the triplet   
                while k > 1 and nums[k] == nums[k+1]:
                    k-=1
            elif curSum < 0:
                j+=1
            else:
                k-=1
            # marks the end of the sweep for a fixed "i"    
            if j >= k:
               i+=1 
               # iterate till last permissible value for "i" and ignore duplicate candidates for 
               # the first position in the triplet
               while i < length-2 and nums[i-1] == nums[i]:
                 i+=1     
               j = i+1
               k = length-1
        return resultList
         
