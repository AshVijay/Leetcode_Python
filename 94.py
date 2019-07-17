"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""


# Definition for a binary tree node.
# class TreeNode: 
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    stack = 0
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        final = []
        self.stack = [root]
        while len(self.stack) >0 :
              cur = self.stack[-1]
              if cur.left != None :
                    self.stack.append(cur.left)
                    cur.left = None
              else:
                    cur = self.stack.pop(-1)         
                    print(cur.val)
                    final.append(cur.val)
                    
                    if cur.right != None:
                        self.stack.append(cur.right)
                        cur.right = None
        return final