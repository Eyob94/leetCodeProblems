/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
 func sumTree(root *TreeNode, val int) int{
        if root == nil{
        return 0
    }
    val = val*2+root.Val
    if root.Left == root.Right{
        return val
    }
    return sumTree(root.Left, val) + sumTree(root.Right, val)
 }
func sumRootToLeaf(root *TreeNode) int {
 return sumTree(root, 0)
    
}