"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.

"""
 
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count=0
        dp = [float("inf") for i in range(len(nums)+1)]
        dp[0]=0
        for i in range(len(nums)):
              if nums[i] ==0 :
                 count-=1
              else:
                 count+=1
              dp[i+1] = count      
        mapper = {}
        for i in range(len(dp)):
           if dp[i] not in mapper.keys() :
             mapper[dp[i]] = [i]
           else:
             mapper[dp[i]].append(i)
        final = 0
        for key in mapper.keys():
             low,high= mapper[key][0]+1, mapper[key][-1]
             if 1+high-low > final :
                      final = 1+high-low
        return final