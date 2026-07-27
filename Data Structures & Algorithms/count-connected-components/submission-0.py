class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjlist = {i : [] for i in range(n)}
        for node, edge in edges:
            adjlist[node].append(edge)
            adjlist[edge].append(node)
        print(adjlist)

        visited = set()

        def dfs(node):
            for n in adjlist[node]:
                if n not in visited:
                    visited.add(n)
                    dfs(n)
        res = 0

        for node in range(n):
            if node not in visited:
                visited.add(n)
                dfs(node)
                res+=1

            
        return res