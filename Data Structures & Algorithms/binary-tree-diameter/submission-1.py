# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.maxd = 0
        self.maxDepth(root)
        return self.maxd
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        maxLeft = self.maxDepth(root.left)
        maxRight = self.maxDepth(root.right)

        self.maxd = max(self.maxd, maxLeft+maxRight)
        return 1 + max(maxLeft, maxRight)