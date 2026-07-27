class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        
        rows, cols = len(grid), len(grid[0])

        q = deque()
        visited = set()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2 and (r, c) not in visited:
                    q.append((r, c))
                    visited.add((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        minutes = 0
        while q and fresh > 0:
            minutes += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc

                    if (nr in range(rows)) and (nc in range(cols)) and grid[nr][nc] == 1 and (nr, nc) not in visited:
                        grid[nr][nc] = 2
                        visited.add((nr, nc))
                        q.append((nr, nc))
                        fresh -= 1
                

        if fresh > 0:
            return -1
        else:
            return minutes
        

                
            



        
        