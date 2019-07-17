"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20], 
  [15,7]
]

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    final = {}
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        self.final = {}
        if root == None:
            return []
        self.recursive_sol(root,0)
        return [ self.final[key] for key in self.final.keys()]
              
    def recursive_sol(self, root , level):
          if level not in self.final.keys():
            self.final[level] = [root.val]
          else:
            self.final[level].append(root.val)
          if root.left != None:
                self.recursive_sol(root.left,level+1)
          if root.right != None:
                self.recursive_sol(root.right,level+1)
            