"""

Print a binary tree in an m*n 2D string array following these rules:

The row number m should be equal to the height of the given binary tree.
The column number n should always be an odd number.
The root node's value (in string format) should be put in the exactly middle of the first row it can be put. The column and the row where the root node belongs will separate the rest space into two parts (left-bottom part and right-bottom part). You should print the left subtree in the left-bottom part and print the right subtree in the right-bottom part. The left-bottom part and the right-bottom part should have the same size. Even if one subtree is none while the other is not, you don't need to print anything for the none subtree but still need to leave the space as large as that for the other subtree. However, if two subtrees are none, then you don't need to leave space for both of them.
Each unused space should contain an empty string "".
Print the subtrees following the same rules.
Example 1:
Input:
     1
    /
   2
Output:
[["", "1", ""], 
 ["2", "", ""]]
Example 2:
Input:
     1
    / \
   2   3
    \
     4
Output:
[["", "", "", "1", "", "", ""],
 ["", "2", "", "", "", "3", ""],
 ["", "", "4", "", "", "", ""]]
Example 3:
Input:
      1
     / \
    2   5
   / 
  3 
 / 
4 
Output:

[["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
 ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
 ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
 ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]
"""



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    final = []
    
    def printTree(self, root: TreeNode) -> List[List[str]]:
       height = 1+self.getHeight(root)
       for i in range(height):
            temp = []
            for j in range(2**height-1):
               temp.append("")
            self.final.append(temp)
        
       self.findString(root,0,0,2**height-1)
       return self.final
    
    def getHeight(self, root):
        if root.left == None and root.right == None:
             return 0
        elif root.right == None and root.left != None:
             return 1+ self.getHeight(root.left)
        elif root.left == None and root.right != None:
             return 1+ self.getHeight(root.right)
        else:
             return 1 + max(self.getHeight(root.left),self.getHeight(root.right))
             
    def findString(self,root, level, left, right):
        if not root: 
             return 
        mid = left + (right - left)//2
        self.final[level][mid] = str(root.val)
        self.findString(root.left, level+1, left, mid-1) 
        self.findString(root.right, level+1, mid+1, right)
        return 