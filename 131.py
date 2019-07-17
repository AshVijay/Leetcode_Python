
"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"], 
  ["a","a","b"]
]
"""

class Solution:
    final = []
    def partition(self, s: str) -> List[List[str]]:
            self.final = []
            self.recurse(s, [])
            return self.final
        
    def recurse(self, remString, tempList):
             if len(remString) == 0  :
                   self.final.append(tempList)
             else:  
                   for i in range(len(remString)):
                          prefix = remString[:i+1]
                          if self.isPalindrome(prefix) :
                                tempList.append(prefix)
                                self.recurse(remString[i+1:],tempList)
                                tempList.pop(-1)
              
    def isPalindrome(self, string ): 
             return string == string[::-1]