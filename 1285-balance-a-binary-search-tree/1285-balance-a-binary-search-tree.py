# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createTree(self, nodes):
        if not nodes:
            return

        ind = len(nodes)//2
        head = TreeNode(nodes[ind].val)

        head.left = self.createTree(nodes[:ind])
        head.right = self.createTree(nodes[ind+1:])

        return head

    def balanceBST(self, root: TreeNode) -> TreeNode:
        stack = []
        curr = root
        res = []

        while curr or stack:
            while curr:
                stack.append(curr)
                curr=curr.left
            
            curr = stack.pop()
            res.append(curr)
            curr = curr.right
        
        return self.createTree(res)

            
