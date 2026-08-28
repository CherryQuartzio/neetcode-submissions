class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set() # for keeping track of teh curren

        # r and c is the current coordinate
        # i is the character position within the word we're looking for
        def dfs(r, c, i):
            if i == len(word): # no more character to search, so we're done
                return True
            
            # invalid cases: out of board, wrong character, or coordinate already visited
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or (r, c) in path):
                return False
            
            # valid character. Keep exploring the rest

            path.add((r, c)) # record this square to prevent revisiting in further recursion
            # pick one of the four direction to go to
            res = (dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1))
            path.remove((r, c)) # done exploring from this square, so removing it from path

            return res

        # we will perform recursion on every starting point on the board
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        
        return False # no path found
