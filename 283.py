"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
"""



class Solution: 
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count =0 
        for i in range(len(nums)):
            if nums[i] ==0 :
                   count+=1
        i=0
        while i < len(nums):
            if nums[i] == 0:
                 nums.pop(i)
            else:
                  i+=1
                    
        list2 = [0]*count
        nums +=list2
        return nums
        