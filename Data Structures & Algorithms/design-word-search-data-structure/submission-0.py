'''Bruteforce would be to search through every inserted string in a list, but using a Trie is more efficient

'''
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        # initialize the Trie
        self.root = TrieNode()

    # same as standard Trie implementation
    def addWord(self, word: str) -> None:
        cur = self.root # start at Trie root

        for char in word:
            if char not in cur.children: # insert new node for non existing word sequence
                cur.children[char] = TrieNode()
            cur = cur.children[char] # go to next node for next char
        cur.endOfWord = True

    # slightly modified for the wildcard character
    def search(self, word: str) -> bool:
        def dfs(begin, root):
            cur = root # start at local root
            for i in range(begin, len(word)):
                char = word[i]

                # we have to use dfs to iterate all possible children for a given wildcard
                if char == '.':
                    for child_node in cur.children.values():
                        if dfs(i + 1, child_node): # if the remaining characters do exist starting from one of the child node
                            return True
                    # no existing child path satisfied from the wildcard        
                    return False
                else:
                    if char not in cur.children:
                        return False # word does not exist
                    cur = cur.children[char] # go to next node for next char

            # word only exist if the last node is marked end of a word. Else, it's only a prefix.
            return cur.endOfWord
        
        return dfs(0, self.root) # start the top of the Trie looking at the full word
        
