# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return
          
        return self.isMirror(root, root)
        
    def isMirror(self, root1, root2):
        if root1 is None and root2 is None:
          return True
        elif root1 is None or root2 is None:
          return False
        
        return root1.val == root2.val and self.isMirror(root1.left, root2.right) and self.isMirror(root1.right, root2.left)