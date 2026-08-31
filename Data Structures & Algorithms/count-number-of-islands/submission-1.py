'''
We want to count all adjacent 1 as one island. To do this, use BFS which involes:
1. process the initial cell, then add it to the queue
2. process all neighboring cells from the cell within the queue
3. repeat until the queue is empty, which means the whole island is processed

NOTE: grid is a matrix of strings, not integer
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # edge: no map = no island
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        visited = set() # prevent revisiting and help keeping track of cells belonging to the same mass
        num_islands = 0

        def bfs(r, c):
            queue = collections.deque() # processed cells that have neighbors to explore
            queue.append((r, c))
            visited.add((r, c))

            # expand the island territorial marking
            while queue:
                row, col = queue.popleft() # change popleft() to just pop() will give a DFS solution!
                neighbors = [[row + 1, col], [row - 1, col], [row, col + 1], [row, col - 1]]

                # process the neighbors
                for nr, nc in neighbors:
                    if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == "1" and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc)) # add to process its neighbors later

        # check every cells for island
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c) # mark all adjacent cells as visited for the same island
                    num_islands += 1

        return num_islands
