# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        stack = [root]
        inorder_index = 0

        for i in range(1, len(preorder)):
            preorder_val = preorder[i]
            node = stack[-1]

            if node.val != inorder[inorder_index]:
                # Create a new node and set it as the left child of the current node
                node.left = TreeNode(preorder_val)
                stack.append(node.left)
            else:
                # Find the node in the stack whose value does not match the inorder traversal
                while stack and stack[-1].val == inorder[inorder_index]:
                    node = stack.pop()
                    inorder_index += 1

                # Set the next preorder value as the right child of the current node
                node.right = TreeNode(preorder_val)
                stack.append(node.right)

        return root
