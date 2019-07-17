"""
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7 

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""


class Solution:
    def longestPalindrome(self, s: str) -> int:
        if s == "" :
             return 0
        from collections import Counter
        count = Counter(s)
        final = 0
        print(count)
        flag = 0
        for i in count.keys():
             if count[i] == 1:
                     flag =1
             if count[i] > 1:
                     if count[i] %2 == 0 :
                             final+= count[i]
                     else:
                             flag =1 
                             final+= (count[i]-1)
        return final+flag