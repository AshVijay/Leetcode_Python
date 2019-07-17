"""
A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
Note:
 
S will have length in range [1, 500].
S will consist of lowercase letters ('a' to 'z') only.
"""

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        i=0
        start = 0
        if len(S) == 0:
             return []
        cur_lim = S.rfind(S[0])
        final= []
        while (i< len(S)):
            if i == cur_lim and cur_lim != len(S)-1:
                final.append(1+cur_lim-start)
                start=cur_lim+1
                cur_lim=S.rfind(S[i+1])
            elif cur_lim == len(S) -1 :
                final.append(1+cur_lim-start)
                break
            else:
                cur_lim = max(S.rfind(S[i]),cur_lim) 
            i+=1 
        return final