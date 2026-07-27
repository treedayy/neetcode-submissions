class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #[2147483647 ,-1             ,0              ,2147483647],
        #[2147483647 ,2147483647     ,2147483647     ,-1],
        #[2147483647 ,-1             ,2147483647     ,-1],
        #[0          ,-1             ,2147483647     ,2147483647]
        INF = 2147483647

        rows, cols = len(grid), len(grid[0])

        visited = set()

        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    visited.add((r, c))
                    q.append((r, c))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr in range(rows) and nc in range(cols)) and (nr, nc) not in visited and grid[nr][nc] == INF:
                    visited.add((nr, nc))
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))



                    
        

