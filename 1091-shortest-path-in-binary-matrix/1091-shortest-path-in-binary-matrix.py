class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:

        from collections import deque
        from typing import List

        rows = len(grid)
        cols = len(grid[0])

        if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
            return -1

        queue = deque([(0, 0 , 1)])

        visited = set()
        visited.add((0, 0))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, 1), (1, -1)]

        while queue:
            r, c, dist = queue.popleft()

            if r == rows -1 and c == cols - 1:
                return dist

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
            
                if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in visited):
                    
                    queue.append((nr, nc, dist + 1))

                    visited.add((nr, nc))

        return - 1





        