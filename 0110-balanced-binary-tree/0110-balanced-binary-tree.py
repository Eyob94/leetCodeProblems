class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def checkBalance(root):
            if not root:
                return [True, 0]
            
            [leftBalanced, leftHeight] = checkBalance(root.left)
            [rightBalanced, rightHeight] = checkBalance(root.right)

            height = max(leftHeight, rightHeight) + 1
            balanced = leftBalanced and rightBalanced and abs(leftHeight-rightHeight) <= 1

            return [balanced, height]

        balanced, height = checkBalance(root)

        return balanced

            



