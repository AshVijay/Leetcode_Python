"""

Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2 
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    stack = []
    def postorderTraversal(self, root: TreeNode) -> List[int]:
            if root == None:
                return []
            self.stack.append(root)
            final = []
            while len(self.stack) > 0:
              cur = self.stack[-1]
              if cur.left != None :
                     self.stack.append(cur.left)
                     cur.left = None
              else:
                   if cur.right != None:
                         self.stack.append(cur.right)
                         cur.right = None
                   else:
                         self.stack.pop(-1)
                         final.append(cur.val)
                         
              
            return final 
            