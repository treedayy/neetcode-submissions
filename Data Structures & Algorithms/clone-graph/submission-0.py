"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        #visited = set()
        #track old to new
        D = {}
        D[node] = Node(node.val)
        source = node
        q = deque()
        q.append(source)
        #visited.add(source)

        while q:
            n = q.popleft()
            for nei_node in n.neighbors:
                if nei_node not in D:
                    #visited.add(nei_node)
                    D[nei_node] = Node(nei_node.val)
                    q.append(nei_node)
                D[n].neighbors.append(D[nei_node])
        return D[node]

