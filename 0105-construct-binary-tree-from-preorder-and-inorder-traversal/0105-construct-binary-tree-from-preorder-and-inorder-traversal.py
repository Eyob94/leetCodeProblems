# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None;
        
        root = TreeNode(preorder[0])
        stack = [root]
        inorder_index = 0

        for val in preorder[1:]:
            node = stack[-1]

            if node.val != inorder[inorder_index]:
                node.left = TreeNode(val)
                stack.append(node.left)
            else:
                while stack and stack[-1].val == inorder[inorder_index]:
                    node = stack.pop()
                    inorder_index += 1
                
                node.right = TreeNode(val)
                stack.append(node.right)

        return root
