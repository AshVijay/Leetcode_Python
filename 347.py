"""
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:
 
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        if nums == []:
              return []
        
        mapper= {}
        final = []
        
        for i in range(len(nums)):
            if nums[i] not in mapper.keys():
                   mapper[nums[i]] = 1
            else:
                   mapper[nums[i]] += 1
            
        q = []
        heapq.heapify(q)
        
        for keys in mapper.keys():
            heapq.heappush(q,[-mapper[keys],keys])
        count = 0
        print(q)
        while (count<k):
             final.append(heapq.heappop(q)[1])
             count+=1
        return final