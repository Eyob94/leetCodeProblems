# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def rec(node, level):
            if node is None:
                return
            
            if len(result) == level:
                result.append(node.val)
            else:
                result[level] = node.val
            
            rec(node.left, level + 1)
            rec(node.right, level + 1)

        rec(root, 0)
        return result

