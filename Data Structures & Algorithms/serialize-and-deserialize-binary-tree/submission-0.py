# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
For this implementation, use comma as the delimiter
'''
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = [] 

        def dfs(node):
            if not node: # represent non nodes as N
                res.append("N")
                return

            # for valid node (in preorder fashion)
            res.append(str(node.val)) # serialize node to string
            dfs(node.left) # serialize left side
            dfs(node.right) # serialize right side
        
        dfs(root) # begin serializing the root
        return ",".join(res) # fully serialized string
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split(",") # extract all characters into each array element
        self.i = 0 # current index. dfs helper acts as a for loop

        def dfs():
            if values[self.i] == "N":
                self.i += 1
                return None # no node to create

            # deserialize (create) node (in preorder fashion)
            node = TreeNode(int(values[self.i])) # new node
            self.i += 1 # increment for the recursive calls to use the next element
            node.left = dfs() # deserialize left side
            node.right = dfs() # deserialize right side

            return node # at the end, this will be the root of the new tree return

        return dfs() # start deserializing at the beginning of the list and return the root in the end
