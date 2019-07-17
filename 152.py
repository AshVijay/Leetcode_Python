"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2: 

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

"""


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Driver function to split nums in a list of segments based on 0s
        """
        prod = -float("inf")
        zeroindices = []
        segments = []
        string = ""
        for i in range(len(nums)):
            if nums[i]==0:
                 zeroindices.append(i)
        i=0
        last = 0
        for i in zeroindices:
            segments.append(nums[last:i])
            last = i+1
        
        if segments== []:
             segments = [nums]
        for segment in segments:
            temp = self.helper(segment)
            if temp>prod:
                 prod = temp
        
        return prod
    
    
    def helper(self,nums):
        """
        To compute segment wise scores   
        """
        countNeg=0
        if len(nums) == 0 :
              return 0
        if len(nums) ==1:
              return nums[0]
            
        for i in range(len(nums)):
              if nums[i] <0:
                     countNeg+=1
        if countNeg %2 ==0 :
              return self.calcProd(nums)
        else:
             left = 0 
             while nums[left] >=0 :
                   left+=1   
             right = len(nums)-1
             while nums[right] >=0:
                   right-=1
        return max(self.calcProd(nums[left+1:]), self.calcProd(nums[:right]))        
            
    def calcProd(self, nums):
        """
        Simple Function to calculate products
        """
        prod = 1 
        for i in range(len(nums)):
              prod*=nums[i]
        return prod