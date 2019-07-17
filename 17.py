"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""
 


class Solution:
    final  = []
    mapper = {"2":['a','b','c'], "3":['d','e','f'], "4":['g','h','i'] ,"5":['j','k','l'] ,"6":['m','n','o'] ,"7":['p','q','r', 's'],"8":['t','u','v'],"9":['w','x','y','z']  }
    def letterCombinations(self, digits: str) -> List[str]:
        digits = list(digits)
        for i in digits:
           print(self.final,i) 
           self.final= self.concLists(i,self.final)
        return self.final
        
        
    def concLists(self, element, final):
            temp = []
            subList = self.mapper[element]
            if len(final) ==0:
                 final = subList
            else:
              for i in subList:
                for j in final:
                    temp.append(j+i)
              final  = temp
            print(final)
            return final
            