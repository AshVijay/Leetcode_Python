"""
226. Invert Binary Tree
Easy

2187

37

Favorite

Share 
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
Trivia:
This problem was inspired by this original tweet by Max Howell:

Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#1

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        head = root
        self.helper(root)
        return head
        
        
    def helper(self, root):
        if root != None: 
              temp = root.left
              root.left = root.right
              root.right = temp
              self.invertTree(root.left)
              self.invertTree(root.right)


#2

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return 
        tempPtr = root.right
        root.right = root.left
        root.left = tempPtr
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root