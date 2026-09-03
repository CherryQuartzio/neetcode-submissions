'''
A tree has two conditions we can use to evaluate its validity:
1. No loop
2. Every nodes are connected

We'll trace the existence of everynode and every available edges to see if they made up one valid tree.
'''

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True # empty tree is a valid tree

        # it will be easier to look up adjacency with a hashmap
        adjacency = {i: [] for i in range(n)}
        for node1, node2 in edges:
            adjacency[node1].append(node2)
            adjacency[node2].append(node1)

        visited = set()

        def dfs(node, prev) -> bool:
            if node in visited:
                return False # loop detected

            visited.add(node) # record into list of visited node
            # Explore the neighbors
            for neighbor in adjacency[node]:
                if neighbor == prev: # don't need to go back to check again
                    continue
                if not dfs(neighbor, node): # loop detected from a neighbor
                    return False

            return True # tree is valid so far

        # For a valid tree, it's possible to visit all other nodes starting from any one node.
        return dfs(0, -1) and len(visited) == n