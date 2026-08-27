# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        current = root # start at the root

        # traverse through the tree. this function will always return a value
        while current:
            if p.val > current.val and q.val > current.val:
                # go to right subtree to keep checking
                current = current.right
            elif p.val < current.val and q.val < current.val:
                # go to left subtree to keep checking
                current = current.left
            else:
                # if value of p and q are not on the same side (left or right), current node is the LCA
                return current