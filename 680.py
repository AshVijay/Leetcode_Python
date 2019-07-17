"""
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.

"""

class Solution:
    def validPalindrome(self, s: str) -> bool: 
        i = 0 
        j = len(s)-1
        flag = 0
        if s == s[::-1] :
                  return True
        while i <= j :
              if s[i] == s[j]:
                  
                      i+=1 
                      j-=1
              else:
                    
                       if  i==0 and s[i:j] == s[j-1::-1] :
                            flag = 1
                            j-=1
                       elif  i!=0 and s[i:j] == s[j-1:i-1:-1] :
                              flag = 1
                              j-=1
                       elif s[i+1:j+1] == s[j:i:-1]:
                              flag = 1
                              i+=1
                       else: 
                              return False
        return flag == 1
    
    