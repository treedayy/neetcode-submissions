# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        q.append((root, float("-inf"), float("inf")))

        while q:
            node = q.popleft()

            if node[0].left:
                if not (node[1] < node[0].left.val < node[0].val):
                    return False
                q.append((node[0].left, node[1], node[0].val))
            if node[0].right: 
                if not (node[0].val < node[0].right.val < node[2]):
                    return False
                q.append((node[0].right, node[0].val, node[2]))
        
        return True