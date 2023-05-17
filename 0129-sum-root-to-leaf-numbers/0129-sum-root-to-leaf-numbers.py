# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def sumNum(root, prev):
            if not root:
                return 0

            prev = prev * 10 + root.val

            if not root.left and not root.right:
                return prev

            left = sumNum(root.left, prev)
            right = sumNum(root.right, prev)

            return left + right

        return sumNum(root, 0)

