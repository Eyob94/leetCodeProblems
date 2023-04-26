# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        result = []
        while stack or root:
            print(result)
            if root:
                stack.append(root)
                root = root.left
            else:
                tmp = stack.pop()
                result.append(tmp.val)
                root = tmp.right
     
        return result

        