"""

Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
"""

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        mapper = {} 
        dp = [0 for i in range(len(T))]
        for i in range(len(T)):
            if T[i] not in mapper.keys():
                  mapper[T[i]] = [i]
            else:
                  mapper[T[i]].append(i)
                    
        for i in range(len(T)):
            temp = T[i]+1
            while temp <= 100:
                  if temp in mapper.keys():
                         indices = mapper[temp]
                         if len(indices) == 0:
                             temp+=1
                             continue
                         while i >= indices[0]:
                                 indices.pop(0)
                                 if len(indices)==0:
                                        break
                         if len(indices)!=0:        
                             dp[i] = indices[0]
                             break   
                         
                  temp +=1

        for i in range(len(dp)):
          if dp[i] != 0:
             dp[i] = dp[i]-i
        return dp