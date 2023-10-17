/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func inOrder(node *TreeNode, result *[]*TreeNode){
    if node == nil{
        return
    }
    inOrder(node.Left, result)
    *result = append(*result, node)
    inOrder(node.Right, result)
}
func increasingBST(root *TreeNode) *TreeNode {
	var newRoot, currentNode *TreeNode

	var inorderTraversal func(node *TreeNode)
	inorderTraversal = func(node *TreeNode) {
		if node == nil {
			return
		}

		inorderTraversal(node.Left)

		if newRoot == nil {
			newRoot = node
			currentNode = node
		} else {
			currentNode.Right = node
			node.Left = nil
			currentNode = node
		}

		inorderTraversal(node.Right)
	}

	inorderTraversal(root)
	return newRoot
}