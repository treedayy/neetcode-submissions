class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])

        seen = set()

        def dfs(r, c) -> int:
            count = 0
            stack = []
            seen.add((r, c))
            stack.append((r, c))
            while stack:
                row, col = stack.pop()
                directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
                for dr, dc in directions:
                    if ((row+dr) in range(rows)) and ((col+dc) in range(cols)) and (grid[row+dr][col+dc] == 1) and ((row+dr, col+dc)) not in seen:
                        stack.append((row+dr, col+dc))
                        seen.add((row+dr, col+dc))
                        count+=1
            return count + 1

                        
            
        maxArea = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in seen:
                    maxArea = max(maxArea, dfs(r, c))
        
        return maxArea
                    
                    
        