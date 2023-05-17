# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        queue = [root]
        bfs = []

        while queue:
            level = []
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.pop(0)
                level.append(node)
            
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            bfs.append(level)

        return [x[-1].val for x in bfs]

