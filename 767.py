"""
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: "" 
Note:
"""

class Solution:
    def reorganizeString(self, S: str) -> str:
        heap = []
        import heapq, collections
        count = collections.Counter(S)
        heapq.heapify(heap)
        for key,value in count.items():
             heapq.heappush(heap,(-value,key))
        final = ""
        while len(heap) != 0:
             value,key=  heapq.heappop(heap)
             print(value, key, final)
             if final == "" :                      #for initial character
                    final += key 
                    value+=1
                    if value<0:
                       heapq.heappush(heap,(value,key))
                    continue
             if final[-1] != key:                  #for cases where last character doesnt match max
                    if value <-1 and len(heap)==0:
                             return ""
                    value +=1
                    final +=key
                    if value<0:
                       heapq.heappush(heap,(value,key))
                    continue
             if final[-1] == key:                  #for cases where last character matches max
                    if len(heap)==0:
                           return ""
                    value1,key1 = heapq.heappop(heap)
                    value1 += 1
                    final += key1
                    if value1<0:
                       heapq.heappush(heap,(value1,key1))
                    heapq.heappush(heap,(value,key))
        