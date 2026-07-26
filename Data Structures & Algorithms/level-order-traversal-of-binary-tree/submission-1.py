# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = []
        q.append(root)
        output = []

        while q:
            qLen = len(q)
            level = []

            for i in range(qLen):
                node = q.pop(0)
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            #node = q.pop(0)
            #print(node.val)
            #if node.left: q.append(node.left)
            #if node.right: q.append(node.right)
            if level:
                output.append(level)
        
        return output
        