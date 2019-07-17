"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true 
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: 
             return False
        i=0
        count = 0
        str_num = str(x)
        while i<len(str_num)//2:
              if str_num[i]==str_num[len(str_num)-i-1]:
                  count+=1
              i+=1
              
        if count == len(str_num)//2: 
              return True
        return False