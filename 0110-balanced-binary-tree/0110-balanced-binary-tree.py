class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def checkBalance(node):
            if not node:
                return 0, True
            
            left_height, left_balanced = checkBalance(node.left)
            right_height, right_balanced = checkBalance(node.right)
            
            height = max(left_height, right_height) + 1
            balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
            
            return height, balanced
        
        _, balanced = checkBalance(root)
        return balanced
