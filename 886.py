
"""
886. Possible Bipartition
Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

Each person may dislike some other people, and they should not go into the same group. 

Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

Return true if and only if it is possible to split everyone into two groups in this way.

 

Example 1:

Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4], group2 [2,3]
Example 2:

Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
Example 3:

Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false
"""

class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        if len(dislikes) == 0 or N == 0:
            return True

        graph = {}
        visited = {}
        color_dict = {}
        for i in range(len(dislikes)):
            if dislikes[i][0] not in graph.keys():
                     graph[dislikes[i][0]] = [dislikes[i][1]]
                     visited[dislikes[i][0]] = 'no'
                     color_dict[dislikes[i][0]] = None  
            else:
                     graph[dislikes[i][0]].append(dislikes[i][1])
            if dislikes[i][1] not in graph.keys():
                     graph[dislikes[i][1]] = [dislikes[i][0]]
                     visited[dislikes[i][1]] = 'no'
                     color_dict[dislikes[i][1]] = None  
            else:
                     graph[dislikes[i][1]].append(dislikes[i][0])
        
        return self.dfs(graph, [ele for ele in graph.keys()][0], 'white', visited, color_dict )

    def dfs(self, graph, node, color, visited, color_dict):
        color_dict[node] = color
        visited[node] = 'yes'       
        for child in graph[node]:
              if visited[child] == 'no':
                     self.dfs(graph, child,  'black' if color == 'white' else 'white', visited, color_dict)
              else:
                  if color_dict[child] == color:
                       return False  
        return True