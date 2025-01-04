"""
11. Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 
Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0 
        right = len(height) - 1
        maxSize = -1
        while left < right:
            curSize = (right - left) * min(height[left], height[right])
            if curSize > maxSize:
                maxSize =  curSize
            # We always move the pointer of the shorter element because even if there is a potential candidate in between, the final selection will never include the shorter element. Potential outcomes for the final selection:
            # 1) It will include both the current left and right elements.
            # 2) It will not include both the current left and right elements.
            # 3) It will include only the larger of the two (current left or right) 
            if height[left] < height[right]:
                left+=1
            elif height[right] < height[left]:
                right-=1
            # If they're both equal, the only possible selection for the final candidates will either include them both or exclude them both
            else:
                left+=1
                right-=1
        return maxSize