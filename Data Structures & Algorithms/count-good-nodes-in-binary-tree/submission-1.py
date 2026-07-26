# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = [(root, root.val)]
        goodNodeCount = 0

        while stack:
            node = stack.pop()
            print(node[1])
            if node[0].val >= node[1]:
                goodNodeCount += 1
            if node[0].left: 
                stack.append((node[0].left, max(node[1], node[0].left.val)))
            if node[0].right: 
                stack.append((node[0].right, max(node[1], node[0].right.val)))

        return goodNodeCount