"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


 

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        from itertools import permutations
        res = []
        for combination in permutations(['(']*n+[')']*n,n*2):
            count = 0
            for i in combination:
                
                if (i == '('):
                     count +=1
                elif (i== ')'):
                     count -= 1
                if(count<0):

                    break
            
            if(count==0):
                  res.append(''.join(combination))
        res = list(dict.fromkeys(res))
        return res