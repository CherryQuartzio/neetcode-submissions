'''
Bruteforce only solution: check every single grid and path for match.
More optimal solution add in a Trie on top of existing bruteforce iteration. How does that work?
- Word search involves pathing from a starting cell. To avoid doing unecessary pathing, we will utilized prefix search from a trie to know what cell to avoid and cut computational cost down to O(1).
- We use DFS for path traversal similarly to Word Search I
'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    # from the usual Trie implementation assumed that its always called from the root
    def addWord(self, word):
        cur = self
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        # create the Trie
        for word in words:
            root.addWord(word)

        ROWS, COLS = len(board), len(board[0])
        result = set()
        visited = set()

        # row, col = current coordinate
        # node = current working node in Trie
        # word = current traced word
        def dfs(row, col, node, word):
            # base case: going out of bound, already visited or not a prefix of any target words
            if (row < 0 or col < 0 or row == ROWS or col == COLS 
            or (row, col) in visited 
            or board[row][col] not in node.children):
                return False

            # continue traversal
            visited.add((row, col)) # to prevent revisiting on the same path
            node = node.children[board[row][col]] # go to next level for next recursion traversal
            word += board[row][col] # add character to word
            if node.isWord: # indicate that we found a word within the search list
                result.add(word)

            # recursion: 4 possible direction on the board
            dfs(row + 1, col, node, word)
            dfs(row - 1, col, node, word)
            dfs(row, col + 1, node, word)
            dfs(row, col - 1, node, word)
            visited.remove((row, col))

        # path from all possible starting cell like Word Search I
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(result)
