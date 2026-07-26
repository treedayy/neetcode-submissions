# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderindex = {value: index for index, value in enumerate(inorder)}
        print(inorderindex)

        self.index = 0

        def dfs(l, r):
            if l > r:
                return None
            rootval = preorder[self.index]
            self.index+=1
            root = TreeNode(rootval)
            mid = inorderindex[rootval]
            root.left = dfs(l, mid-1)
            root.right = dfs(mid+1, r)
            return root


        return dfs(0, len(inorder) - 1)