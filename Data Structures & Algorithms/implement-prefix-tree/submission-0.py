class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:
    '''
    A trie will be a tree made up of TrieNodes. It's slightly different in that:
    - It contains multiple children
    - The node does not contain it's own value. That is referenced from prior node via the dictionary
    - It has a boolean to indicate if it's the end of a word
    '''

    def __init__(self):
        self.root = TrieNode() # we will have a Trie root that does not contain any character
        
    def insert(self, word: str) -> None:
        cur = self.root # start at root TrieNode

        for char in word: # for every character of the word
            if char not in cur.children: # create a new node for nonexisting Trie sequence
                cur.children[char] = TrieNode()

            # proceed to next node in lower level for next character
            cur = cur.children[char]

        # end of word reach and mark endOfWord
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root # start at root TrieNode

        for char in word: # for every character of the word
            if char not in cur.children: # word does not exist in Trie
                return False

            # proceed to next node in lower level for next character
            cur = cur.children[char]

        # all linked nodes exist, but check whether it's a recorded word or just a prefix
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root # start at root TrieNode

        for char in prefix: # for every character of the prefix
            if char not in cur.children: # prefix does not exist in Trie
                return False

            # proceed to next node in lower level for next character
            cur = cur.children[char]

        # all linked nodes exist. Regardless if this is a recorded word, it's a prefix
        return True
        
        