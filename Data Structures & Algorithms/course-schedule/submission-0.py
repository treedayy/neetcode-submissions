class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            graph[a].append(b)

        visiting = set()

        def dfs(node):
            if node in visiting:
                return False
            if graph[node] == []:
                return True
            
            visiting.add(node)
            for n in graph[node]:
                if not dfs(n):
                    return False
            visiting.remove(node)
            graph[node] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True