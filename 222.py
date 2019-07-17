"""
Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input: 
    1 
   / \
  2   3
 / \  /
4  5 6

Output: 6

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None




class Solution:
    count = 1
    def countNodes(self, root: TreeNode) -> int:
        if root != None:
           self.recurse(root)
        else:
            return 0
        return self.count
    def recurse(self, root):
        if root.left != None:
            self.count+=1
            self.recurse(root.left)
        if root.right != None:
            self.count += 1
            self.recurse(root.right)
        

