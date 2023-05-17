# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not inorder or not preorder:
            return None
  
        head = TreeNode(preorder[0])
        headIndex = inorder.index(head.val)
        newPre = preorder[1:]

        head.left  = self.buildTree(preorder[1:headIndex+1], inorder[:headIndex])
        head.right = self.buildTree(preorder[headIndex+1:], inorder[headIndex+1:])

        

        return head
        