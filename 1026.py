"""
Given the root of a binary tree, find the maximum value V for which there exists different nodes A and B where V = |A.val - B.val| and A is an ancestor of B.

(A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.)
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None 

class Solution:
    #maxx = 0
    def maxAncestorDiff(self, root: TreeNode) -> int:
        children = []
        children = self.get_children(root,children)
        
        
        if(root.left == None and root.right == None):
             return 0
        elif(root.left == None and root.right != None):
            
            return max(self.maxAncestorDiff(root.right), max([ abs(root.val - i) for i in children]))
            
        elif(root.right == None and root.left != None):

            return max(self.maxAncestorDiff(root.left),max([abs(root.val -i) for i in children]))
        
        else:

            return max(self.maxAncestorDiff(root.left), self.maxAncestorDiff(root.right),max([ abs(root.val - i) for i in children]),max([abs(root.val -i) for i in children]))   
    
    def get_children(self,root : TreeNode,children) :
        if(root.left != None):
             children.append(root.left.val)
             self.get_children(root.left,children)
        if(root.right != None):
             children.append(root.right.val)
             self.get_children(root.right,children)
        return children