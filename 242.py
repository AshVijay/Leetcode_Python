"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = {}
        # iterate through first string and create an alphabet count map
        for i in range(len(s)):
            if s[i] not in counter:
                counter[s[i]] = 1
            else:
                counter[s[i]] += 1
        
        # iterate through second string and re-calculate counter map 
        for i in range(len(t)):
            if t[i] not in counter:
                counter[t[i]] = -1 # assign a negative value for all characters present in "t" that is not there in "s"
            else:
                counter[t[i]] -= 1
        
        for key in counter.keys():
            if counter[key] != 0:
                return False
        return True