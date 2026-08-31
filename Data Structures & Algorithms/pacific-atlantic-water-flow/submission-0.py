'''
Instead of bruteforcing every cell and see where it can lead to, the more efficient approach is to see what cells can be reach indiviually from both oceans starting from their shores.
'''

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set() # maintain the cells that can flow water into the respective ocean

        def dfs(r, c, ocean, prev_height):
            # false case: if the cell is out of bound of the grid or have lower elevation (water can't flow down to the shores) or already recorded in the set
            if r < 0 or c < 0 or r == ROWS or c == COLS or (r, c) in ocean or heights[r][c] < prev_height:
                return False
            
            # confirmed: cell can flow water into the ocean
            ocean.add((r, c))
            # explore the neighbors in DFS iteration
            dfs(r + 1, c, ocean, heights[r][c])
            dfs(r - 1, c, ocean, heights[r][c])
            dfs(r, c + 1, ocean, heights[r][c])
            dfs(r, c - 1, ocean, heights[r][c])

            # since we passed in the ocean set as a recursion parameter, we do not need ocean.remove((r, c))

        # find reachable cells to each ocean from the vertical shores
        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])

        # find reachable cells to each ocean from the horizontal shores
        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])

        # determine the cells that can reach both oceans (if they're in both set)
        # problem wants the result to be a list of list, so can't do set union as a shortcut
        result = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])

        return result