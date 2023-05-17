# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        answer = []

        def rec(node, level):
            if node is None:
                return

            if len(answer) == level:
                answer.append(node.val)         
            else:
                answer[level] = node.val

            left = rec(node.left, level+1)
            right = rec(node.right, level+1)

        rec(root, 0)

        return answer
        

