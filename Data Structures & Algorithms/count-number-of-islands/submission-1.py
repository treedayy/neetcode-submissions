class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])

        seen = set()

        def bfs(row, col):
            q = deque()
            seen.add((row, col))
            q.append((row, col))
            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc, in directions:
                    if ((row + dr) in range(rows)) and ((col + dc) in range(cols)) and grid[row+dr][col+dc] == "1" and ((row+dr, col+dc) not in seen):
                        q.append((row+dr, col+dc))
                        seen.add((row+dr, col+dc))

        islands = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in seen: 
                    bfs(row, col)
                    #run bfs on (row, col)
                    islands += 1
                
        return islands