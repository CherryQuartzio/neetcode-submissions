"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

For any graph problems, using a hashmap is recommended.
Runtime: O(|V| + |E|)
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldNewEquivalent = {} # keeping track of cloned node to prevent duplicate

        # helper clone method that recursively iterate using DFS
        def dfs(node):
            if node in oldNewEquivalent: # node already cloned so no further processing needs
                return oldNewEquivalent[node]

            node_copy = Node(node.val) # NEW node with the same value
            oldNewEquivalent[node] = node_copy
            for neighbor in node.neighbors: # for every neighbor of this node, we link all their copies as our neighbor
                node_copy.neighbors.append(dfs(neighbor))
            
            return node_copy # return either to CloneGraph or previous dfs call wanting to add it as a neighbor
                
        return dfs(node) if node else None # empty graph edge case