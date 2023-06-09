# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], Min=float('-inf'), Max=float('inf')) -> bool:
        if not root:
            return True
    
        if root.val <= Min or root.val >= Max:
            return False
        
        left = self.isValidBST(root.left, Min, root.val)
        right =self.isValidBST(root.right, root.val, Max)
        
        return left and right
        