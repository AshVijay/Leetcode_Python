"""
You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.

You always start to construct the left child node of the parent first if it exists.

Example:
Input: "4(2(3)(1))(6(5))"
Output: return the tree root node representing the following tree:

       4
     /   \ 
    2     6
   / \   / 
  3   1 5   
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def str2tree(self, s: str) -> TreeNode:
         if s == "":
            return None
         root = TreeNode(s[0]) 
         root.left,root.right = self.formTree(root,s[1:])
        
    def formTree(self, root, string):
          stack = []
          l1,r1,l2,r2 = 0,0,0,len(string)-1
        
          if string == "" :
                return None
         
          for i in range(len(string)):
             item = string[i]
             if item == "(":
                    stack.append(item)
             elif item == ")":
                    stack.pop()
             if len(stack) ==0 :
                r1= i
                l2 = i+1
                break
          print(string[l1+1:r1])
          print(string[l2+1:r2])
                
          root.left = self.formTree(root,string[l1+2:r1])
          root.right = self.formTree(root,string[l2+2:r2-1])
          return root.left, root.right   
                    