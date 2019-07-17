
"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar" 
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        i = 0
        j=0
        mapper = {}
        while i < len(s):
             if s[i] not in mapper.keys() and t[j] not in mapper.values(): 
                  mapper[s[i]] = t[j] 
                  i+=1
                  j+=1
                  continue
             elif (s[i] not in mapper.keys() and t[j] in mapper.values()) or  (s[i] in mapper.keys() and t[j] != mapper[s[i]]):
                  return False

             i+=1
             j+=1
                  
        return True