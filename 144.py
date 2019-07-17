
"""
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1 
    \
     2
    /
   3

Output: [1,2,3]

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    stack = []
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
             return []
        self.stack.append(root)
        final = []
        while len(self.stack) > 0:
          cur =  self.stack.pop(-1)
          print(cur.val)
          final.append(cur.val)
          if cur.right != None :
                self.stack.append(cur.right)
          if cur.left != None:
                self.stack.append(cur.left)
        return final 
            
                