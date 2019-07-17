
"""
3. Longest Substring Without Repeating Characters
Medium

6372

367

Favorite 

Share
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
         pal = [ [0 for r in range(len(s))] for l in range(len(s))]
         pal_len =  [ [0 for r in range(len(s))] for l in range(len(s))]
         for l in range(len(s)):
                for r in range(len(s)):
                  if l == r :
                        pal[l][r] = 1
                        pal_len[l][r] = 1
                  if l<r:
                    
                    if s[l]==s[r] and pal[l+1][r-1]:
                           pal[l][r] = 1
                           pal_len[l][r] = 1+r-l
                        
                    elif s[l]!=s[r]:
                            pal[l][r] = 0 
                            pal_len[l][r] = max(pal_len[l][r-1],pal_len[l+1][r],pal_len[l+1][r])
         max_val = 0
         final = (0,0)
         print(pal_len)
         for i in range(len(s)):
              for j in range(len(s)):
                    if i >=j :
                         if pal_len[i][j] > max_val:
                                 final = (i,j)
         return s[final[0]:final[1]+1]