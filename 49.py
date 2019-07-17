"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:
 

"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag_dict = {}
        if strs == []:
              return []
        for i in range(len(strs)):
            temp_str = str(sorted(strs[i]))
            if temp_str not in anag_dict.keys():
                anag_dict[temp_str] = [strs[i]] 
            else:
                anag_dict[temp_str].append(strs[i])
        final = []
        for keys in anag_dict.keys():
             final.append(anag_dict[keys])
        return final