"""
Given a list of words, each word consists of English lowercase letters.

Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2.  For example, "abc" is a predecessor of "abac".

A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.

Return the longest possible length of a word chain with words chosen from the given list of words.

  

Example 1:

Input: ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: one of the longest word chain is "a","ba","bda","bdca".
"""


class Solution:
    hashmap = {}
    table = {}
    def longestStrChain(self, words: List[str]) -> int:
        for i in words :
              if(len(i) not in self.hashmap):
                    self.hashmap[len(i)] = [i]
                    self.table[len(i)] = 1
              else :
                    self.hashmap[len(i)].append(i)
        for key in self.hashmap.keys():
            for element in self.hashmap[key]: 
                self.dpSol(key, element)
        return 1+ sorted(self.table.items(), key= lambda items:items[1])[-1][1]
        
    def dpSol(self, key, item1):
        import itertools
        if key is max(self.hashmap.keys()):
          return 0
        else:
          list2=  self.hashmap[key+1]
          for item2 in list2:

                     for i in  ["".join(item) for item in [ items for items in itertools.permutations(item2,len(item2)) ]]:
                       if item1 in i:
                         
                         self.table[key] = 1+ self.dpSol(key+1, item2)
                         return self.table[key]
                     else:
                         return 1